from datetime import datetime
from tabulate import tabulate

class BankAccount:
    """
    A simple Bank Account class to handle deposits, withdrawals, and balance checks.
    """

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.tran = {
            'time': [],
            'previous balance': [],
            'transaction': [],
            'Balance': []
        }

    def deposit(self, amount):
        prev_bal = self.balance
        self.balance += amount
        print(f"\nDeposited: {amount}. New Balance: {self.balance}")
        self.transaction_history(amount, prev_bal)

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nInsufficient funds.")
        else:
            prev_bal = self.balance
            self.balance -= amount
            print(f"\nWithdrew: {amount}. New Balance: {self.balance}")
            self.transaction_history(-amount, prev_bal)

    def get_balance(self):
        print(f"\nCurrent Balance: {self.balance}")
        return self.balance

    def transaction_history(self, tran_amnt, prev_bal):
        self.tran['time'].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.tran['previous balance'].append(prev_bal)
        self.tran['transaction'].append(tran_amnt)
        self.tran['Balance'].append(self.balance)

    def view_transactions(self):
        if not self.tran['time']:
            print("\nNo transactions yet.")
            return

        table_data = []
        for i in range(len(self.tran['time'])):
            table_data.append([
                self.tran['time'][i],
                self.tran['previous balance'][i],
                self.tran['transaction'][i],
                self.tran['Balance'][i]
            ])

        print("\nTransaction History:")
        print(tabulate(table_data, headers=["Time", "Previous Balance", "Transaction", "New Balance"], tablefmt="grid"))


# Global lists to store account information
accounts = []
n = []


def acct_create():
    wrongtypelimit = 0
    while True:
        acct_title = input('\nEnter your name: ')
        if acct_title in n:
            print('User already exists.')
            wrongtypelimit += 1
        else:
            n.append(acct_title)
            try:
                init_bal = int(input('Enter initial deposit: '))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            accounts.append(BankAccount(acct_title, init_bal))
            print("\n✅ Your account was successfully created.")

            o = input('Do you want to add another account (y/n): ').lower()
            if o != 'y':
                break

        if wrongtypelimit == 3:
            print("Too many attempts. Exiting.")
            break


def atm_menu(account):
    while True:
        print(f"\nWelcome, {account.owner}!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            account.get_balance()
        elif choice == '2':
            try:
                amount = int(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            try:
                amount = int(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            account.view_transactions()
        elif choice == '5':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Try again.")


# Example usage
if __name__ == "__main__":
    acct_create()
    if accounts:
        atm_menu(accounts[0])
