from auth import authenticate_user
def deposit(name, pin, amount):
    if amount <= 0:
        print("\nDeposit amount must be positive.")
        return
    account = authenticate_user(name, pin)
    if account:
        account["balance"] += amount
        transaction_record = f"Deposited: +₹{amount:.2f}"
        account["transactions"].append(transaction_record)
        print(f"\nSuccessfully deposited ₹{amount:.2f}.")
        print(f"Your new balance is: ₹{account['balance']:.2f}")
    else:
        print("\nAuthentication failed. Invalid name or PIN.")
