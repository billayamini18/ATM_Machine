# Contains the function to view an account's transaction history.
from auth import authenticate_user

def transaction_history(name, pin):
    #Shows all recorded deposits and withdrawals for an account.
    account = authenticate_user(name, pin)
    if account:
        print(f"\n--- Transaction History for {account['name']} ---")
        #If transactions are empty
        if not account["transactions"]:
            print("No transactions found.")
        else:
            for transaction in account["transactions"]:
                print(transaction)
        print("---------------------------------")
    else:
        print("\nAuthentication failed. Invalid name or PIN.")