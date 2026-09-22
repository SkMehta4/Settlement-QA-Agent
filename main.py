# PS-8: Settlement Q&A Agent
# A basic Python project for tracing payment settlements


# -------------------------------
# MOCK GATEWAY DATA
# -------------------------------

gateway_data = {
    "TXN1001": {
        "date": "2026-09-20",
        "amount": 1500,
        "status": "PROCESSED"
    },

    "TXN1002": {
        "date": "2026-09-20",
        "amount": 2500,
        "status": "PROCESSED"
    },

    "TXN1003": {
        "date": "2026-09-21",
        "amount": 3200,
        "status": "FAILED"
    },

    "TXN1004": {
        "date": "2026-09-21",
        "amount": 1800,
        "status": "PROCESSED"
    },

    "TXN1005": {
        "date": "2026-09-22",
        "amount": 5000,
        "status": "PROCESSED"
    }
}


# -------------------------------
# MOCK BANK DATA
# -------------------------------

bank_data = {
    "TXN1001": {
        "date": "2026-09-20",
        "amount": 1500,
        "status": "SETTLED"
    },

    "TXN1002": {
        "date": "2026-09-20",
        "amount": 2500,
        "status": "PENDING"
    },

    "TXN1003": {
        "date": "2026-09-21",
        "amount": 3200,
        "status": "NOT_RECEIVED"
    },

    "TXN1004": {
        "date": "2026-09-21",
        "amount": 1800,
        "status": "SETTLED"
    },

    "TXN1005": {
        "date": "2026-09-22",
        "amount": 5000,
        "status": "PENDING"
    }
}


# -------------------------------
# MOCK LEDGER DATA
# -------------------------------

ledger_data = {
    "TXN1001": {
        "date": "2026-09-20",
        "amount": 1500,
        "status": "RECORDED"
    },

    "TXN1002": {
        "date": "2026-09-20",
        "amount": 2500,
        "status": "RECORDED"
    },

    "TXN1003": {
        "date": "2026-09-21",
        "amount": 3200,
        "status": "NOT_RECORDED"
    },

    "TXN1004": {
        "date": "2026-09-21",
        "amount": 1800,
        "status": "RECORDED"
    },

    "TXN1005": {
        "date": "2026-09-22",
        "amount": 5000,
        "status": "RECORDED"
    }
}


# -------------------------------
# TRACE TRANSACTION
# -------------------------------

def trace_transaction(transaction_id):

    print("\n" + "=" * 55)
    print("             TRANSACTION SETTLEMENT REPORT")
    print("=" * 55)

    gateway = gateway_data.get(transaction_id)
    bank = bank_data.get(transaction_id)
    ledger = ledger_data.get(transaction_id)

    # Check whether transaction exists
    if gateway is None:
        print("\nTransaction ID not found.")
        print("Please check the Transaction ID and try again.")
        return

    # Basic transaction information
    print("\nTransaction ID :", transaction_id)
    print("Date           :", gateway["date"])
    print("Amount         :", gateway["amount"])

    # -------------------------------
    # GATEWAY INFORMATION
    # -------------------------------

    print("\n--- Gateway Record ---")

    print("Status :", gateway["status"])
    print("Amount :", gateway["amount"])
    print("Date   :", gateway["date"])

    # -------------------------------
    # BANK INFORMATION
    # -------------------------------

    print("\n--- Bank Record ---")

    if bank is not None:
        print("Status :", bank["status"])
        print("Amount :", bank["amount"])
        print("Date   :", bank["date"])
    else:
        print("Bank record not found.")

    # -------------------------------
    # LEDGER INFORMATION
    # -------------------------------

    print("\n--- Ledger Record ---")

    if ledger is not None:
        print("Status :", ledger["status"])
        print("Amount :", ledger["amount"])
        print("Date   :", ledger["date"])
    else:
        print("Ledger record not found.")

    # List for storing problems
    exceptions = []

    # -------------------------------
    # CHECK GATEWAY
    # -------------------------------

    if gateway["status"] != "PROCESSED":
        exceptions.append(
            "Gateway did not process the transaction."
        )

    # -------------------------------
    # CHECK BANK
    # -------------------------------

    if bank is None:

        exceptions.append(
            "Bank record is missing."
        )

    elif bank["status"] == "PENDING":

        exceptions.append(
            "Bank settlement is still pending."
        )

    elif bank["status"] == "NOT_RECEIVED":

        exceptions.append(
            "Bank did not receive the transaction."
        )

    # -------------------------------
    # CHECK LEDGER
    # -------------------------------

    if ledger is None:

        exceptions.append(
            "Ledger record is missing."
        )

    elif ledger["status"] == "NOT_RECORDED":

        exceptions.append(
            "Transaction is not recorded in the ledger."
        )

    # -------------------------------
    # CHECK AMOUNT CONSISTENCY
    # -------------------------------

    if bank is not None:

        if gateway["amount"] != bank["amount"]:

            exceptions.append(
                "Gateway and bank amounts do not match."
            )

    if ledger is not None:

        if gateway["amount"] != ledger["amount"]:

            exceptions.append(
                "Gateway and ledger amounts do not match."
            )

    # -------------------------------
    # CHECK DATE CONSISTENCY
    # -------------------------------

    if bank is not None:

        if gateway["date"] != bank["date"]:

            exceptions.append(
                "Gateway and bank dates do not match."
            )

    if ledger is not None:

        if gateway["date"] != ledger["date"]:

            exceptions.append(
                "Gateway and ledger dates do not match."
            )

    # -------------------------------
    # FINAL SETTLEMENT EXPLANATION
    # -------------------------------

    print("\n--- Settlement Explanation ---")

    if len(exceptions) == 0:

        print("Settlement completed successfully.")
        print("Gateway, bank, and ledger records are consistent.")

    else:

        print("Settlement requires attention.")

        print("\nException List:")

        for exception in exceptions:

            print("-", exception)

    print("\n" + "=" * 55)


# -------------------------------
# SEARCH BY DATE
# -------------------------------

def search_by_date(search_date):

    found = False

    print("\n" + "=" * 55)
    print("TRANSACTIONS FOR DATE:", search_date)
    print("=" * 55)

    for transaction_id in gateway_data:

        transaction = gateway_data[transaction_id]

        if transaction["date"] == search_date:

            found = True

            print(
                transaction_id,
                "| Amount:",
                transaction["amount"],
                "| Status:",
                transaction["status"]
            )

    if not found:

        print("No transactions found for this date.")


# -------------------------------
# MAIN MENU
# -------------------------------

def main():

    print("\n" + "=" * 55)
    print("              SETTLEMENT Q&A AGENT")
    print("=" * 55)

    print("\nThis program traces transactions across:")
    print("1. Gateway")
    print("2. Bank")
    print("3. Ledger")

    while True:

        print("\n" + "-" * 55)
        print("MENU")
        print("-" * 55)

        print("1. Search Transaction")
        print("2. Search Transactions by Date")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        # -------------------------------
        # OPTION 1
        # -------------------------------

        if choice == "1":

            transaction_id = input(
                "\nEnter Transaction ID: "
            ).strip().upper()

            trace_transaction(transaction_id)

        # -------------------------------
        # OPTION 2
        # -------------------------------

        elif choice == "2":

            search_date = input(
                "\nEnter date (YYYY-MM-DD): "
            ).strip()

            search_by_date(search_date)

        # -------------------------------
        # OPTION 3
        # -------------------------------

        elif choice == "3":

            print("\nThank you for using Settlement Q&A Agent.")
            print("Program ended.")
            break

        # -------------------------------
        # INVALID OPTION
        # -------------------------------

        else:

            print("\nInvalid choice.")
            print("Please enter 1, 2, or 3.")


# -------------------------------
# START PROGRAM
# -------------------------------

if __name__ == "__main__":
    main()