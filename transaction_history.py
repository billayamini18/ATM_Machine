from auth import authenticate_user
def transaction_history(name, pin):
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
