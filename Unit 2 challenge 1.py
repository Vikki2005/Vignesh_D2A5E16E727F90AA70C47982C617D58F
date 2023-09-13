class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Balance for {self._account_holder_name}: ${self._account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    account = BankAccount("1234567890", "John Doe", 1000.00)
    
    account.display_balance()  # Display initial balance
    account.deposit(500.00)    # Deposit $500
    account.withdraw(200.00)   # Withdraw $200
    account.display_balance()  # Display updated balanc
