from abc import ABC, abstractmethod
from enum import Enum


# Singleton Pattern: ATMMachine should be a Singleton
class ATM:
    _instance = None

    @staticmethod
    def get_instance():
        if ATM._instance is None:
            ATM._instance = ATM()
        return ATM._instance

    def __init__(self):
        if ATM._instance is not None:
            raise Exception("This is a Singleton class.")
        self.account = None
        self.state = IdleState(self)

    def set_account(self, account):
        self.account = account

    def change_state(self, state):
        self.state = state

    def authenticate(self, pin):
        self.state.authenticate(pin)

    def perform_transaction(self, transaction):
        self.state.perform_transaction(transaction)

    def cancel_transaction(self):
        self.state.cancel_transaction()


# Account Class (SRP - handles user account operations)
class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def authenticate_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


# Enum for Transaction Types
class TransactionType(Enum):
    DEPOSIT = "Deposit"
    WITHDRAWAL = "Withdrawal"
    CHECK_BALANCE = "Check Balance"


# Strategy Pattern: Transaction Class (allows different transaction types)
class Transaction(ABC):
    @abstractmethod
    def execute(self, atm, account):
        pass


# Concrete Transaction Types
class DepositTransaction(Transaction):
    def __init__(self, amount):
        self.amount = amount

    def execute(self, atm, account):
        account.deposit(self.amount)
        print(f"Deposited ${self.amount}. New balance: ${account.get_balance()}")


class WithdrawTransaction(Transaction):
    def __init__(self, amount):
        self.amount = amount

    def execute(self, atm, account):
        if account.withdraw(self.amount):
            print(f"Withdrew ${self.amount}. New balance: ${account.get_balance()}")
        else:
            print("Insufficient funds.")


class CheckBalanceTransaction(Transaction):
    def execute(self, atm, account):
        print(f"Current balance: ${account.get_balance()}")


# Observer Pattern: Transaction Observer for Notification
class TransactionObserver(ABC):
    @abstractmethod
    def update(self, transaction):
        pass


class TransactionNotification(TransactionObserver):
    def update(self, transaction):
        print("Transaction completed successfully!")


# State Pattern: States for ATM Machine
class ATMState(ABC):
    @abstractmethod
    def authenticate(self, pin):
        pass

    @abstractmethod
    def perform_transaction(self, transaction):
        pass

    @abstractmethod
    def cancel_transaction(self):
        pass


# Concrete States for the ATM Machine
class IdleState(ATMState):
    def __init__(self, atm):
        self.atm = atm

    def authenticate(self, pin):
        if self.atm.account.authenticate_pin(pin):
            print("Authentication successful!")
            self.atm.change_state(AuthenticatedState(self.atm))
        else:
            print("Authentication failed.")

    def perform_transaction(self, transaction):
        print("Please authenticate first.")

    def cancel_transaction(self):
        print("No transaction to cancel.")


class AuthenticatedState(ATMState):
    def __init__(self, atm):
        self.atm = atm

    def authenticate(self, pin):
        print("Already authenticated.")

    def perform_transaction(self, transaction):
        print(f"Performing {transaction.__class__.__name__}...")
        transaction.execute(self.atm, self.atm.account)
        self.atm.change_state(IdleState(self.atm))

    def cancel_transaction(self):
        print("Cancelling transaction...")
        self.atm.change_state(IdleState(self.atm))


# Main code to run the ATM machine
if __name__ == "__main__":
    # Create an account
    account = Account("12345", "1234", 1000)  # Account with PIN '1234' and balance $1000
    atm = ATM.get_instance()
    atm.set_account(account)

    # Observer Pattern: Transaction Notification
    notification = TransactionNotification()

    # Authenticate the user
    pin = input("Enter your PIN: ")
    atm.authenticate(pin)

    # Perform a deposit transaction
    deposit = DepositTransaction(500)
    atm.perform_transaction(deposit)
    notification.update(deposit)

    # Perform a withdrawal transaction
    withdraw = WithdrawTransaction(300)
    atm.perform_transaction(withdraw)
    notification.update(withdraw)

    # Perform a balance check transaction
    check_balance = CheckBalanceTransaction()
    atm.perform_transaction(check_balance)
    notification.update(check_balance)
