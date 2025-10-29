import json
import os
from datetime import datetime
from tabulate import tabulate
import sys


class BankAccount:
    """A simple Bank Account class to handle deposits, withdrawals, and balance checks."""

    def __init__(self, owner, pin, balance=0, transactions=None):
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.transactions = transactions if transactions else {
            'time': [],
            'previous balance': [],
            'transaction': [],
            'Balance': []
        }

    def _timestamp(self):
        """Return current time."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def deposit(self, amount):
        """Deposit money."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        prev_bal = self.balance
        self.balance += amount
        self._add_transaction(amount, prev_bal)
        print(f"\n✅ Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw money."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("\n❌ Insufficient funds.")
            return
        prev_bal = self.balance
        self.balance -= amount
        self._add_transaction(-amount, prev_bal)
        print(f"\n💸 Withdrew: {amount}. New Balance: {self.balance}")

    def check_balance(self):
        """Show current balance."""
        print(f"\n💰 Current Balance: {self.balance}")
        return self.balance

    def _add_transaction(self, tran_amount, prev_bal):
        """Add a transaction to the record."""
        self.transactions['time'].append(self._timestamp())
        self.transactions['previous balance'].append(prev_bal)
        self.transactions['transaction'].append(tran_amount)
        self.transactions['Balance'].append(self.balance)

    def view_transactions(self):
        """Display transaction history in a table."""
        if not self.transactions['time']:
            print("\nNo transactions yet.")
            return
        table_data = []
        for i in range(len(self.transactions['time'])):
            table_data.append([
                self.transactions['time'][i],
                self.transactions['previous balance'][i],
                self.transactions['transaction'][i],
                self.transactions['Balance'][i]
            ])
        print("\n📜 Transaction History:")
        print(tabulate(table_data, headers=["Time", "Previous Balance", "Transaction", "New Balance"], tablefmt="grid"))


# ---------- File Handling ----------

def load_accounts(filename="accounts.json"):
    """Load all accounts from JSON."""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_accounts(accounts, filename="accounts.json"):
    """Save all accounts to JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=4)


# ---------- Core Functionalities ----------

def create_account():
    """Create a new user account."""
    accounts = load_accounts()

    name = input("\nEnter your name: ").strip()
    if name in accounts:
        print("⚠️ Account already exists with this name.")
        return

    while True:
        pin = input("Set a 4-digit PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            break
        else:
            print("PIN must be exactly 4 digits.")

    try:
        init_balance = float(input("Enter initial deposit: "))
    except ValueError:
        print("Invalid amount. Account not created.")
        return

    new_account = BankAccount(name, pin, init_balance)
    accounts[name] = {
        "pin": pin,
        "balance": init_balance,
        "transactions": new_account.transactions
    }
    save_accounts(accounts)
    print(f"\n✅ Account created successfully for {name}!")


def login():
    """Login to an existing account."""
    accounts = load_accounts()
    name = input("\nEnter your name: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()

    if name in accounts and accounts[name]["pin"] == pin:
        print(f"\n👋 Welcome {name}!")
        data = accounts[name]
        account = BankAccount(name, pin, data["balance"], data["transactions"])
        atm_menu(account, accounts)
    else:
        print("❌ Invalid credentials. Please try again.")


def atm_menu(account, accounts):
    """Main ATM menu after login."""
    while True:
        print(f"\n--- ATM Menu ({account.owner}) ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Logout")
        print("6. Exit ATM")

        choice = input("Select an option: ")

        if choice == '1':
            account.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            account.view_transactions()
        elif choice == '5':
            # Save before logout and return to main menu
            accounts[account.owner] = {
                "pin": account.pin,
                "balance": account.balance,
                "transactions": account.transactions
            }
            save_accounts(accounts)
            print("\n👋 Logged out successfully.")
            return  # go back to main menu
        elif choice == '6':
            # Save and exit the whole program
            accounts[account.owner] = {
                "pin": account.pin,
                "balance": account.balance,
                "transactions": account.transactions
            }
            save_accounts(accounts)
            print("\n🛑 Exiting ATM system... Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

        # Auto-save after every operation
        accounts[account.owner] = {
            "pin": account.pin,
            "balance": account.balance,
            "transactions": account.transactions
        }
        save_accounts(accounts)


# ---------- Main Program ----------

def main():
    while True:
        print("\n=== Welcome to the Python ATM ===")
        print("1. Create New Account")
        print("2. Login")
        print("3. Logout / Exit ATM System")

        choice = input("Select an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("\n👋 You have been logged out of the ATM system. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
