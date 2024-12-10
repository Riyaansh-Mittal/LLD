from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def get_id(self):
        return self.user_id

    def get_name(self):
        return self.name


class UserManager:
    def __init__(self):
        self.users = []
        self.user_map = {}

    def add_user(self, user_id, name):
        user = User(user_id, name)
        self.users.append(user)
        self.user_map[user_id] = user

    def get_user(self, user_id):
        return self.user_map.get(user_id)

    def get_all_users(self):
        return self.users


class TransactionManager:
    def __init__(self, users):
        self.transactions = {
            user.get_id(): {other.get_id(): Decimal('0.00') for other in users}
            for user in users
        }

    def adjust_transaction(self, payer_id, user_id, amount):
        self.transactions[user_id][payer_id] -= amount
        self.transactions[payer_id][user_id] += amount

    def get_balances(self, user_id=None):
        if user_id:
            return self.transactions[user_id]
        return self.transactions


class Split(ABC):
    @abstractmethod
    def perform_split(self, amount, users, payer, details, transaction_manager):
        pass


class EqualSplit(Split):
    def perform_split(self, amount, users, payer, details, transaction_manager):
        split_amount = (Decimal(amount) / len(users)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        for user in users:
            if user != payer:
                transaction_manager.adjust_transaction(payer.get_id(), user.get_id(), split_amount)


class PercentSplit(Split):
    def perform_split(self, amount, users, payer, percentages, transaction_manager):
        if sum(percentages) != 100:
            raise ValueError("Percentages must add up to 100.")
        for user, percentage in zip(users, percentages):
            if user != payer:
                split_amount = (Decimal(amount) * (Decimal(percentage) / 100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                transaction_manager.adjust_transaction(payer.get_id(), user.get_id(), split_amount)


class ExactSplit(Split):
    def perform_split(self, amount, users, payer, exact_amounts, transaction_manager):
        if sum(exact_amounts) != amount:
            raise ValueError("Exact amounts must sum to the total amount.")
        for user, exact_amount in zip(users, exact_amounts):
            if user != payer:
                split_amount = Decimal(exact_amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                transaction_manager.adjust_transaction(payer.get_id(), user.get_id(), split_amount)


class SplitFactory:
    @staticmethod
    def get_split(expense_type):
        if expense_type == 'EQUAL':
            return EqualSplit()
        elif expense_type == 'PERCENT':
            return PercentSplit()
        elif expense_type == 'EXACT':
            return ExactSplit()
        else:
            raise ValueError("Invalid expense type")


class ExpenseProcessor:
    def __init__(self, user_manager, transaction_manager):
        self.user_manager = user_manager
        self.transaction_manager = transaction_manager

    def add_expense(self, expense_type, amount, user_ids, payer_id, details=None):
        users = [self.user_manager.get_user(uid) for uid in user_ids]
        payer = self.user_manager.get_user(payer_id)

        if not payer or any(user is None for user in users):
            raise ValueError("Invalid payer or user IDs")

        split = SplitFactory.get_split(expense_type)
        split.perform_split(amount, users, payer, details, self.transaction_manager)


class Wallet:
    def __init__(self):
        self.user_manager = UserManager()
        self.transaction_manager = None
        self.expense_processor = None

    def setup_wallet(self, users):
        for user_id, name in users:
            self.user_manager.add_user(user_id, name)
        self.transaction_manager = TransactionManager(self.user_manager.get_all_users())
        self.expense_processor = ExpenseProcessor(self.user_manager, self.transaction_manager)

    def show_balances(self, user_id=None):
        transactions = self.transaction_manager.get_balances(user_id)
        if user_id:
            self._show_user_balances(user_id, transactions)
        else:
            self._show_all_balances(transactions)

    def _show_user_balances(self, user_id, balances):
        user = self.user_manager.get_user(user_id)
        if not user:
            print("Invalid user ID")
            return
        has_balance = False
        for other_id, balance in balances.items():
            if balance < 0:
                print(f"{user.get_name()} owes {self.user_manager.get_user(other_id).get_name()}: {-balance}")
                has_balance = True
            elif balance > 0:
                print(f"{self.user_manager.get_user(other_id).get_name()} owes {user.get_name()}: {balance}")
                has_balance = True
        if not has_balance:
            print("No balances")

    def _show_all_balances(self, transactions):
        has_balance = False
        for user_id, user_balances in transactions.items():
            for other_id, balance in user_balances.items():
                if balance < 0:
                    print(f"{self.user_manager.get_user(user_id).get_name()} owes {self.user_manager.get_user(other_id).get_name()}: {-balance}")
                    has_balance = True
        if not has_balance:
            print("No balances")

    def add_expense(self, expense_type, amount, user_ids, payer_id, details=None):
        self.expense_processor.add_expense(expense_type, amount, user_ids, payer_id, details)


# Main Execution
wallet = Wallet()
wallet.setup_wallet([
    ('u1', 'User1'),
    ('u2', 'User2'),
    ('u3', 'User3'),
    ('u4', 'User4')
])

wallet.add_expense('EQUAL', 1000, ['u1', 'u2', 'u3', 'u4'], 'u1')
wallet.show_balances('u4')
wallet.show_balances('u1')
wallet.add_expense('EXACT', 1250, ['u2', 'u3'], 'u1', [370, 880])
wallet.show_balances()
wallet.add_expense('PERCENT', 1200, ['u1', 'u2', 'u3', 'u4'], 'u4', [40, 20, 20, 20])
wallet.show_balances('u1')
wallet.show_balances()