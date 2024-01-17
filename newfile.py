
class User:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)

class ATM:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def create_user(self, user_id, pin, initial_balance):
        if user_id not in self.users:
            user = User(user_id, pin, initial_balance)
            self.users[user_id] = user
            print("User created successfully.")
        else:
            print("User already exists.")

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            return True
        else:
            print("Authentication failed. Invalid user ID or PIN.")
            return False

    def display_menu(self):
        print("1. Transaction History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def perform_transaction(self, option):
        if option == 1:
            self.show_transaction_history()
        elif option == 2:
            self.withdraw()
        elif option == 3:
            self.deposit()
        elif option == 4:
            self.transfer()
        elif option == 5:
            print("Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.current_user.transaction_history:
            print(transaction)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if 0 < amount <= self.current_user.balance:
            self.current_user.balance -= amount
            self.current_user.add_transaction(f"Withdrew ${amount}. New balance: ${self.current_user.balance}")
            print(f"Withdrew ${amount}. New balance: ${self.current_user.balance}")
        else:
            print("Invalid amount or insufficient balance.")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        if amount > 0:
            self.current_user.balance += amount
            self.current_user.add_transaction(f"Deposited ${amount}. New balance: ${self.current_user.balance}")
            print(f"Deposited ${amount}. New balance: ${self.current_user.balance}")
        else:
            print("Invalid amount.")

    def transfer(self):
        recipient_id = input("Enter recipient's user ID: ")
        if recipient_id in self.users and recipient_id != self.current_user.user_id:
            amount = float(input("Enter the amount to transfer: $"))
            if 0 < amount <= self.current_user.balance:
                self.current_user.balance -= amount
                self.current_user.add_transaction(f"Transferred ${amount} to {recipient_id}. New balance: ${self.current_user.balance}")
                self.users[recipient_id].balance += amount
                self.users[recipient_id].add_transaction(f"Received ${amount} from {self.current_user.user_id}. New balance: ${self.users[recipient_id].balance}")
                print(f"Transferred ${amount} to {recipient_id}. New balance: ${self.current_user.balance}")
            else:
                print("Invalid amount or insufficient balance.")
        else:
            print("Recipient not found or invalid recipient.")

if __name__ == "__main__":
    atm = ATM()

    # Create a user with predefined user ID and PIN
    atm.create_user("Shivam", "0007", 3000.0)

    while True:
        if atm.current_user is None:
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            if atm.authenticate_user(user_id, pin):
                print(f"Welcome, {user_id}!")
            else:
                continue

        atm.display_menu()
        option = int(input("Select an option (1-5): "))
        atm.perform_transaction(option)