from auth import authenticate_user
def check_balance(name, pin):
    account = authenticate_user(name, pin)
    if account:
        print(f"\nYour current balance is: ₹{account['balance']:.2f}")
    else:

        print("\nAuthentication failed. Invalid name or PIN.")
