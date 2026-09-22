# Settlement Q&A Agent

A simple **Settlement Q&A Agent** built using Python. This project allows users to search transactions and check their settlement status across gateway, bank, and ledger records.

## Features

* Search transaction using Transaction ID
* Search transactions by date
* Check gateway status
* Check bank settlement status
* Check ledger status
* Detect pending and failed settlements
* Compare transaction amounts
* Compare transaction dates
* Display settlement exceptions
* Simple menu-driven interface
* No external Python libraries required

## Technologies Used

* Python
* Dictionaries
* Functions
* Loops
* Conditional Statements

## Project Structure

```text
Settlement-QA-Agent/
│
├── README.md
└── main.py
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/ashu192708/Settlement-QA-Agent.git
```

Go to the project folder:

```bash
cd Settlement-QA-Agent
```

Run the program:

```bash
python3 main.py
```

## How It Works

The program contains mock records for:

* Gateway
* Bank
* Ledger

The user can enter a Transaction ID such as:

```text
TXN1001
```

The program checks the transaction in all three systems and displays the available records.

It then checks whether:

* The gateway processed the transaction
* The bank settled the transaction
* The transaction was recorded in the ledger
* The amount is consistent
* The date is consistent

If an issue is found, the program displays it as an exception.

## Example Transactions

```text
TXN1001 → Successful settlement
TXN1002 → Bank settlement pending
TXN1003 → Failed / not received
TXN1004 → Successful settlement
TXN1005 → Bank settlement pending
```

## Requirements

* Python 3.x
* No external libraries required

## Note

This project uses mock transaction data for demonstration purposes. It does not connect to real banks, payment gateways, or financial systems.
