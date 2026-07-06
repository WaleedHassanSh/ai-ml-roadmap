# CS50x Week 9 Flask Projects

This folder contains the CS50x Week 9 Flask projects:

1. **Birthdays**
2. **C$50 Finance**

Recommended local folder structure:

```text
cs50x/
└── week-09-flask/
    ├── birthdays/
    └── finance/
```

---

## 1. Birthdays

### Folder Structure

```text
birthdays/
├── app.py
├── birthdays.db
├── static/
│   └── styles.css
└── templates/
    └── index.html
```

### Goal

Create a Flask web application that stores and displays friends' birthdays.

### Main Requirements

- Show all birthdays from `birthdays.db` on the homepage.
- Add a form where users can enter:
  - name
  - month
  - day
- Insert submitted birthdays into the `birthdays` table.
- Re-render the homepage after submission.

### Run Locally

From inside the `birthdays` folder:

```bash
flask run
```

### Submit

```bash
submit50 cs50/problems/2026/x/birthdays
```

---

## 2. Finance

### Folder Structure

```text
finance/
├── app.py
├── finance.db
├── helpers.py
├── requirements.txt
├── static/
│   ├── favicon.ico
│   ├── I_heart_validator.png
│   └── styles.css
└── templates/
    ├── apology.html
    ├── buy.html
    ├── history.html
    ├── index.html
    ├── layout.html
    ├── login.html
    ├── quote.html
    ├── quoted.html
    ├── register.html
    ├── sell.html
    └── add_cash.html
```

### Goal

Create a Flask web application where users can register, log in, quote stocks, buy stocks, sell stocks, and view transaction history.

### Main Required Routes

| Route | Purpose |
|---|---|
| `/register` | Register a new user |
| `/quote` | Look up a stock price |
| `/buy` | Buy shares |
| `/` | Show portfolio |
| `/sell` | Sell shares |
| `/history` | Show transaction history |

### Personal Touch

At least one extra feature is required. Recommended simple option:

```text
Add Cash
```

This can allow users to add extra cash to their account.

---

## Recommended Database Table for Finance Transactions

You can create a table like this:

```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price REAL NOT NULL,
    type TEXT NOT NULL,
    transacted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```

Suggested values for `type`:

```text
buy
sell
```

---

## Run Finance Locally

From inside the `finance` folder:

```bash
flask run
```

---

## Check Finance

```bash
check50 cs50/problems/2026/x/finance
```

---

## Style Check

```bash
style50 app.py
```

---

## Submit Finance

```bash
submit50 cs50/problems/2026/x/finance
```

---

## Important Cleanup Before Submission

Before submitting, remove unnecessary generated folders/files such as:

```text
__pycache__/
flask_session/
```

Your submitted folder should only contain files needed for the project.

---

## Testing Checklist

### Birthdays

- Add a valid birthday.
- Confirm it appears in the table.
- Try empty fields.
- Try invalid month/day values.
- Reload the page and confirm saved birthdays still appear.

### Finance

Test the following:

- Register a new user.
- Log in successfully.
- Quote a valid stock symbol.
- Try an invalid stock symbol.
- Buy valid shares.
- Try buying more shares than affordable.
- Try zero, negative, decimal, or text shares.
- Confirm portfolio updates correctly.
- Sell some shares.
- Try selling more shares than owned.
- Confirm history shows all buy/sell transactions.
- Test the personal touch feature.

---

## Suggested Local Path

Linux / WSL / macOS:

```bash
~/code/cs50x/week-09-flask/
```

Windows:

```text
C:\Users\Waleed\code\cs50x\week-09-flask\
```

---

## Notes

- Run each Flask app from inside its own project folder.
- Do not run `flask run` from the parent `week-09-flask` folder.
- Use parameterized SQL queries with `?` placeholders.
- Do not use f-strings or string concatenation for SQL queries.
- Always validate form input server-side, not only in HTML.
