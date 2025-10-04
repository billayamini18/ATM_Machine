# Contains the function to add money to an account.
from auth import authenticate_user

def deposit(name, pin, amount):
    # Adds money to an account and records the transaction.
    if amount <= 0:
        print("\nDeposit amount must be positive.")
        return
    # Checks user entered correct name and pin.
    account = authenticate_user(name, pin)
    if account:
        account["balance"] += amount
        transaction_record = f"Deposited: +₹{amount:.2f}"
        account["transactions"].append(transaction_record)
        print(f"\nSuccessfully deposited ₹{amount:.2f}.")
        print(f"Your new balance is: ₹{account['balance']:.2f}")
    else:
        print("\nAuthentication failed. Invalid name or PIN.")