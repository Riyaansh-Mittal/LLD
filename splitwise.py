from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP


class User:
    def __init__(self, user_id, name, email, phone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone

    def get_id(self):
        return self.user_id

    def get_name(self):
        return self.name


class UserManager:
    def __init__(self):
        self.users = {}
        
    def add_user(self, user_id, name, email, phone):
        user = User(user_id, name, email, phone)
        self.users[user_id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return self.users.values()


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
        percentages = [Decimal(str(amount)) for amount in percentages]
        if sum(percentages) != 100:
            raise ValueError("Percentages must add up to 100.")
        for user, percentage in zip(users, percentages):
            if user != payer:
                split_amount = (Decimal(amount) * (Decimal(percentage) / 100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                transaction_manager.adjust_transaction(payer.get_id(), user.get_id(), split_amount)


class ExactSplit(Split):
    def perform_split(self, amount, users, payer, exact_amounts, transaction_manager):
        # Convert exact amounts to Decimals
        exact_amounts = [Decimal(str(amount)) for amount in exact_amounts]
        
        if sum(exact_amounts) != Decimal(str(amount)):
            raise ValueError("Exact amounts must sum to the total amount.")
        
        for user, exact_amount in zip(users, exact_amounts):
            if user != payer:
                split_amount = exact_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
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


class ExpenseSharingApp:
    def __init__(self):
        self.user_manager = UserManager()
        self.transaction_manager = None
        self.expense_processor = None

    def add_user(self, user_id, name, email, phone):
        self.user_manager.add_user(user_id, name, email, phone)

    def setup_transactions(self):
        self.transaction_manager = TransactionManager(self.user_manager.get_all_users())
        self.expense_processor = ExpenseProcessor(self.user_manager, self.transaction_manager)

    def process_input(self, command):
        if command.startswith("SHOW"):
            parts = command.split()
            if len(parts) == 1:
                return self._show_balances()
            else:
                return self._show_user_balances(parts[1])

        elif command.startswith("EXPENSE"):
            parts = command.split()
            payer_id = parts[1]
            amount = Decimal(parts[2])
            num_users = int(parts[3])
            user_ids = parts[4:4 + num_users]
            expense_type = parts[4 + num_users]
            details = parts[5 + num_users:] if len(parts) > 5 + num_users else None
            self.expense_processor.add_expense(expense_type, amount, user_ids, payer_id, details)
            return "Expense added successfully."

    def _show_balances(self):
        transactions = self.transaction_manager.get_balances()
        return self._format_balances(transactions)

    def _show_user_balances(self, user_id):
        user = self.user_manager.get_user(user_id)
        if not user:
            return "Invalid user ID."
        transactions = self.transaction_manager.get_balances(user_id)
        return self._format_user_balances(user_id, transactions)

    def _format_balances(self, transactions):
        output = []
        for user_id, balances in transactions.items():
            for other_id, balance in balances.items():
                if balance < 0:
                    output.append(f"{self.user_manager.get_user(user_id).get_name()} owes {self.user_manager.get_user(other_id).get_name()}: {-balance}")
        return "\n".join(output) if output else "No balances."

    def _format_user_balances(self, user_id, balances):
        output = []
        user = self.user_manager.get_user(user_id)
        for other_id, balance in balances.items():
            if balance < 0:
                output.append(f"{user.get_name()} owes {self.user_manager.get_user(other_id).get_name()}: {-balance}")
            elif balance > 0:
                output.append(f"{self.user_manager.get_user(other_id).get_name()} owes {user.get_name()}: {balance}")
        return "\n".join(output) if output else "No balances."


if __name__ == "__main__":
    app = ExpenseSharingApp()
    
    # Adding users
    app.add_user("u1", "User1", "user1@example.com", "1234567890")
    app.add_user("u2", "User2", "user2@example.com", "1234567891")
    app.add_user("u3", "User3", "user3@example.com", "1234567892")
    app.add_user("u4", "User4", "user4@example.com", "1234567893")
    
    app.setup_transactions()

    # Sample Input/Output
    print(app.process_input("SHOW"))  # No balances
    print(app.process_input("SHOW u1"))  # No balances

    print(app.process_input("EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL"))
    print(app.process_input("SHOW u4"))
    print(app.process_input("SHOW u1"))

    print(app.process_input("EXPENSE u1 1250 2 u2 u3 EXACT 370 880"))
    print(app.process_input("SHOW"))

    print(app.process_input("EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20"))
    print(app.process_input("SHOW u1"))
    print(app.process_input("SHOW"))
