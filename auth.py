# Shared utility for user authentication.
from data import accounts
def authenticate_user(name, pin):
    """
    Finds and authenticates a user based on name and PIN.
    Returns the user's account dictionary if successful, otherwise None.
    """
    for account in accounts:
        # if both and pin is correct 
        if account["name"].lower() == name.lower() and account["pin"] == pin:
            return account
    return None