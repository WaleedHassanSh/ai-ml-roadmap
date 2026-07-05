-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find the crime scene report for the theft on Humphrey Street on July 28, 2025.
SELECT description
FROM crime_scene_reports
WHERE year = 2025
AND month = 07
AND day = 28
AND street = "Humphrey Street";

-- Find vehicles that exited the bakery parking lot within ten minutes of the theft.
SELECT activity, license_plate
FROM bakery_security_logs
WHERE year = 2025
AND month = 07
AND day = 28
AND hour >= 10
AND minute >= 15
AND minute <= 25
AND activity = "exit";

-- Identify the people whose cars left the bakery parking lot during the relevant time window.
SELECT *
FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2025
    AND month = 07
    AND day = 28
    AND hour >= 10
    AND minute >= 15
    AND minute <= 25
    AND activity = "exit"
);

-- Find all withdrawals made at the Leggett Street ATM on the day of the theft.
SELECT *
FROM atm_transactions
WHERE year = 2025
AND month = 07
AND day = 28
AND atm_location LIKE "Leggett Street"
AND transaction_type = "withdraw";

-- Find bank accounts belonging to suspects whose vehicles exited the bakery parking lot.
SELECT *
FROM bank_accounts
WHERE person_id IN (
    SELECT id
    FROM people
    WHERE license_plate IN (
        SELECT license_plate
        FROM bakery_security_logs
        WHERE year = 2025
        AND month = 07
        AND day = 28
        AND hour >= 10
        AND minute >= 15
        AND minute <= 25
        AND activity = "exit"
    )
);

-- Find which bakery-exit suspects made a withdrawal at the Leggett Street ATM.
SELECT *
FROM atm_transactions
WHERE year = 2025
AND month = 07
AND day = 28
AND atm_location LIKE "Leggett Street"
AND transaction_type = "withdraw"
AND account_number IN (
    SELECT account_number
    FROM bank_accounts
    WHERE person_id IN (
        SELECT id
        FROM people
        WHERE license_plate IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE year = 2025
            AND month = 07
            AND day = 28
            AND hour >= 10
            AND minute >= 15
            AND minute <= 25
            AND activity = "exit"
        )
    )
);

-- Retrieve the bank account records connected to the relevant ATM withdrawals.
SELECT *
FROM bank_accounts
WHERE account_number IN (
    SELECT account_number
    FROM atm_transactions
    WHERE year = 2025
    AND month = 07
    AND day = 28
    AND atm_location LIKE "Leggett Street"
    AND transaction_type = "withdraw"
    AND account_number IN (
        SELECT account_number
        FROM bank_accounts
        WHERE person_id IN (
            SELECT id
            FROM people
            WHERE license_plate IN (
                SELECT license_plate
                FROM bakery_security_logs
                WHERE year = 2025
                AND month = 07
                AND day = 28
                AND hour >= 10
                AND minute >= 15
                AND minute <= 25
                AND activity = "exit"
            )
        )
    )
);

-- Identify the suspects who both left the bakery parking lot and withdrew money from the ATM.
SELECT *
FROM people
WHERE id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE year = 2025
        AND month = 07
        AND day = 28
        AND atm_location LIKE "Leggett Street"
        AND transaction_type = "withdraw"
        AND account_number IN (
            SELECT account_number
            FROM bank_accounts
            WHERE person_id IN (
                SELECT id
                FROM people
                WHERE license_plate IN (
                    SELECT license_plate
                    FROM bakery_security_logs
                    WHERE year = 2025
                    AND month = 07
                    AND day = 28
                    AND hour >= 10
                    AND minute >= 15
                    AND minute <= 25
                    AND activity = "exit"
                )
            )
        )
    )
);

-- Find all flights leaving Fiftyville on the day after the theft.
SELECT *
FROM flights
WHERE year = 2025
AND month = 07
AND day = 29
AND origin_airport_id = (
    SELECT id
    FROM airports
    WHERE city = "Fiftyville"
);

-- Read the witness interviews from the day of the theft for additional clues.
SELECT transcript
FROM interviews
WHERE year = 2025
AND month = 07
AND day = 28;

-- Find passengers on the earliest flight who also match the bakery parking lot clue.
SELECT *
FROM passengers
WHERE flight_id IN (
    SELECT id
    FROM flights
    WHERE year = 2025
    AND month = 07
    AND day = 29
    AND hour = 08
    AND minute = 20
    AND origin_airport_id = (
        SELECT id
        FROM airports
        WHERE city = "Fiftyville"
    )
)
AND passport_number IN (
    SELECT passport_number
    FROM people
    WHERE license_plate IN (
        SELECT license_plate
        FROM bakery_security_logs
        WHERE year = 2025
        AND month = 07
        AND day = 28
        AND hour >= 10
        AND minute >= 15
        AND minute <= 25
        AND activity = "exit"
    )
);

-- Identify the thief by combining the bakery, ATM, flight, and short phone call evidence.
SELECT *
FROM people
WHERE passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE year = 2025
        AND month = 07
        AND day = 29
        AND hour = 08
        AND minute = 20
        AND origin_airport_id = (
            SELECT id
            FROM airports
            WHERE city = "Fiftyville"
        )
    )
    AND passport_number IN (
        SELECT passport_number
        FROM people
        WHERE license_plate IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE year = 2025
            AND month = 07
            AND day = 28
            AND hour >= 10
            AND minute >= 15
            AND minute <= 25
            AND activity = "exit"
        )
    )
)
AND passport_number IN (
    SELECT passport_number
    FROM people
    WHERE id IN (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN (
            SELECT account_number
            FROM atm_transactions
            WHERE year = 2025
            AND month = 07
            AND day = 28
            AND atm_location LIKE "Leggett Street"
            AND transaction_type = "withdraw"
            AND account_number IN (
                SELECT account_number
                FROM bank_accounts
                WHERE person_id IN (
                    SELECT id
                    FROM people
                    WHERE license_plate IN (
                        SELECT license_plate
                        FROM bakery_security_logs
                        WHERE year = 2025
                        AND month = 07
                        AND day = 28
                        AND hour >= 10
                        AND minute >= 15
                        AND minute <= 25
                        AND activity = "exit"
                    )
                )
            )
        )
    )
)
AND phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE year = 2025
    AND month = 07
    AND day = 28
    AND duration < 60
);

-- Find the short phone call made by Bruce on the day of the theft.
SELECT *
FROM phone_calls
WHERE year = 2025
AND month = 07
AND day = 28
AND duration < 60
AND caller IN (
    SELECT phone_number
    FROM people
    WHERE name = "Bruce"
);

-- Identify the receiver of Bruce's short phone call, revealing the accomplice.
SELECT *
FROM people
WHERE phone_number = (
    SELECT receiver
    FROM phone_calls
    WHERE year = 2025
    AND month = 07
    AND day = 28
    AND duration < 60
    AND caller IN (
        SELECT phone_number
        FROM people
        WHERE name = "Bruce"
    )
);

-- Find the destination city of the earliest flight taken by the thief.
SELECT *
FROM airports
WHERE id = 4;
