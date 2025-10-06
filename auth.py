from data import accounts
def authenticate_user(name, pin):
    for account in accounts:
        # if both and pin is correct 
        if account["name"].lower() == name.lower() and account["pin"] == pin:
            return account

    return None

