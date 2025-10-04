# The main entry point for the ATM application.
# Import each function from its respective module
from check_balance import check_balance
from deposit import deposit
from withdraw import withdraw
from transaction_history import transaction_history

def run_atm():
    # Displays the main menu and handles user input 
    while True:
        print("\n===== ATM Machine =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        
        choice_input = input("Enter your choice (1-5): ")

        # Validate that the choice is a number
        if not choice_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        choice = int(choice_input)

        if choice == 5:
            print("\nThank you for using the ATM!")
            break

        if choice in [1, 2, 3, 4]:
            name = input("Enter your name: ")
            pin_input = input("Enter your PIN: ")

            # Validate that the PIN is a number
            if not pin_input.isdigit():
                print("\nInvalid PIN format. Please enter numbers only.")
                continue
            
            pin = int(pin_input)

            if choice == 1:
                check_balance(name, pin)
            
            elif choice == 2:
                amount_input = input("Enter amount to deposit: ₹")
                # Validate that the amount is a valid number (integer or float)
                if amount_input.replace('.', '', 1).isdigit():
                    amount = float(amount_input)
                    deposit(name, pin, amount)
                else:
                    print("\nInvalid amount. Please enter a valid number.")

            elif choice == 3:
                amount_input = input("Enter amount to withdraw: ₹")
                # Validate that the amount is a valid number (integer or float)
                if amount_input.replace('.', '', 1).isdigit():
                    amount = float(amount_input)
                    withdraw(name, pin, amount)
                else:
                    print("\nInvalid amount. Please enter a valid number.")
            
            elif choice == 4:
                transaction_history(name, pin)
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

# --- Run the program ---
run_atm()