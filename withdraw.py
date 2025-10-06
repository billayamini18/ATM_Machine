from auth import authenticate_user
def withdraw(name, pin, amount):
    if amount <= 0:
        print("\nWithdrawal amount must be positive.")
        return

    account = authenticate_user(name, pin)
    if account:
        if account["balance"] >= amount:
            account["balance"] -= amount
            transaction_record = f"Withdrew: -₹{amount:.2f}"
            account["transactions"].append(transaction_record)
            print(f"\nSuccessfully withdrew ₹{amount:.2f}.")
            print(f"Your remaining balance is: ₹{account['balance']:.2f}")
        else:
            print("\nInsufficient balance for this withdrawal.")
    else:

        print("\nAuthentication failed. Invalid name or PIN.")
