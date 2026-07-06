from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import apology, login_required, lookup, usd
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    shares = db.execute(
        """
        SELECT symbol,
        COALESCE(SUM(CASE WHEN transaction_type = 'buy' THEN shares ELSE 0 END), 0)
        -
        COALESCE(SUM(CASE WHEN transaction_type = 'sell' THEN shares ELSE 0 END), 0)
        as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
        """,
        session["user_id"],
    )

    portfolio = []

    grand_total = 0

    for share in shares:
        port = {}

        result = lookup(share["symbol"])

        if result is None:
            continue
        port["symbol"] = share["symbol"]
        port["shares"] = share["total_shares"]
        port["current_price"] = result["price"]
        port["total_value"] = result["price"] * share["total_shares"]

        grand_total += result["price"] * share["total_shares"]

        portfolio.append(port)

    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

    return render_template(
        "index.html",
        portfolio=portfolio,
        cash=user_cash[0]["cash"],
        grand_total=grand_total + user_cash[0]["cash"],
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol or not shares:
            return apology("Input fields cannot be empty")

        result = lookup(symbol)

        if not result:
            return apology("Invalid symbol")

        try:
            shares = int(shares)
        except ValueError:
            return apology("Share should be a number")

        if shares < 1:
            return apology("Shares should be positive integer")

        total_cash = shares * result["price"]

        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )

        user_cash = user_cash[0]["cash"]

        if total_cash > user_cash:
            return apology("Cannot afford")

        db.execute(
            "INSERT INTO transactions(user_id, symbol, shares, price, transaction_type) VALUES (?, ?, ?, ?, ?)",
            session["user_id"],
            result["symbol"],
            shares,
            result["price"],
            "buy",
        )

        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?",
            user_cash - total_cash,
            session["user_id"],
        )

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute(
        "SELECT * FROM transactions WHERE user_id = ? ORDER BY timestamp DESC",
        session["user_id"],
    )
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Empty symbol")

        result = lookup(symbol)

        if not result:
            return apology("Invalid symbol")

        return render_template("quoted.html", result=result)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("Input field cannot be empty")

        if password != confirmation:
            return apology("Passwords do not match")

        password_hash = generate_password_hash(
            password, method="scrypt", salt_length=16
        )

        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                username,
                password_hash,
            )
        except ValueError:
            return apology("Duplicate username")

        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not shares or not symbol:
            return apology("Input field cannot be empty")

        try:
            shares = int(shares)

            if shares < 1:
                return apology("Shares must be a positive integer")
        except ValueError:
            return apology("Shares must be a integer")

        owned_shared = db.execute(
            """
            SELECT
            COALESCE(SUM(CASE WHEN transaction_type = 'buy' THEN shares ELSE 0 END), 0)
            -
            COALESCE(SUM(CASE WHEN transaction_type = 'sell' THEN shares ELSE 0 END), 0)
            as total_shares
            FROM transactions
            WHERE user_id = ? AND symbol = ?
            """,
            session["user_id"],
            symbol,
        )

        if owned_shared[0]["total_shares"] < shares:
            return apology("Cannot sell shares")

        result = lookup(symbol)

        if not result:
            return apology("Invalid symbol")

        db.execute(
            "INSERT INTO transactions(user_id, symbol, shares, price, transaction_type) VALUES (?, ?, ?, ?, ?)",
            session["user_id"],
            result["symbol"],
            shares,
            result["price"],
            "sell",
        )

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        cash = cash[0]["cash"] + (shares * result["price"])

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        return redirect("/")

    else:
        symbols = db.execute(
            """
            SELECT symbol
            FROM transactions
            WHERE user_id = ?
            GROUP by symbol
            HAVING
            SUM(CASE WHEN transaction_type = 'buy' THEN shares ELSE 0 END)
            -
            SUM(CASE WHEN transaction_type = 'sell' THEN shares ELSE 0 END) > 0
            """,
            session["user_id"],
        )
        return render_template("sell.html", symbols=symbols)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    if request.method == "POST":
        cash = request.form.get("cash")

        if not cash:
            return apology("Input field cannot be empty")

        try:
            cash = float(cash)

            if cash < 1:
                return apology("Cash must be a positive value")

        except ValueError:
            return apology("Cash must be a number")

        current_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )

        cash += current_cash[0]["cash"]

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        return redirect("/")

    else:
        return render_template("add_cash.html")
