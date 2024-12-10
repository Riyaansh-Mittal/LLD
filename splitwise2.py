from abc import ABC, abstractmethod

# User class
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def get_id(self):
        return self.user_id

    def get_name(self):
        return self.name

# Abstract Split class
class Split(ABC):
    @abstractmethod
    def operation(self, amount, users, payer, details, wallet):
        pass

# Base Split class for shared logic
class BaseSplit(Split):
    def adjust_transactions(self, payer, user, amount, wallet):
        wallet.transactions[user.get_id()][payer.get_id()] -= amount
        wallet.transactions[payer.get_id()][user.get_id()] += amount

# Equal Split class
class EqualSplit(BaseSplit):
    def operation(self, amount, users, payer, details, wallet):
        split_amount = round(amount / len(users), 2)
        for user in users:
            if user != payer:
                self.adjust_transactions(payer, user, split_amount, wallet)

# Percent Split class
class PercentSplit(BaseSplit):
    def operation(self, amount, users, payer, percentages, wallet):
        if sum(percentages) != 100:
            raise ValueError("Percentages must add up to 100.")
        split_amounts = [round((percentage / 100) * amount, 2) for percentage in percentages]
        for i, user in enumerate(users):
            if user != payer:
                self.adjust_transactions(payer, user, split_amounts[i], wallet)

# Exact Split class
class ExactSplit(BaseSplit):
    def operation(self, amount, users, payer, exact_amounts, wallet):
        if sum(exact_amounts) != amount:
            raise ValueError("Exact amounts must sum to the total amount.")
        for i, user in enumerate(users):
            if user != payer:
                self.adjust_transactions(payer, user, round(exact_amounts[i], 2), wallet)

# Wallet class
class Wallet:
    def __init__(self):
        self.users = [
            User('u1', 'User1'),
            User('u2', 'User2'),
            User('u3', 'User3'),
            User('u4', 'User4')
        ]
        self.user_map = {user.get_id(): user for user in self.users}  # Quick access to users by ID
        self.transactions = {user.get_id(): {user1.get_id(): 0 for user1 in self.users} for user in self.users}

    def show(self, user_id=''):
        if user_id == '':
            has_balance = False
            for user in self.users:
                for other_user in self.users:
                    if user.get_id() != other_user.get_id():
                        balance = round(self.transactions[user.get_id()][other_user.get_id()], 2)
                        if balance < 0:
                            print(f"{user.get_name()} owes {other_user.get_name()}: {-balance}")
                            has_balance = True
            if not has_balance:
                print("No balances")
        else:
            has_balance = False
            user = self.user_map[user_id]
            # First print those who owe the user money (balance < 0)
            for other_user in self.users:
                if user_id != other_user.get_id():
                    balance = round(self.transactions[user_id][other_user.get_id()], 2)
                    if balance < 0:
                        print(f"{user.get_name()} owes {other_user.get_name()}: {-balance}")
                        has_balance = True
            # Then print those who the user owes money to (balance > 0)
            for other_user in self.users:
                if user_id != other_user.get_id():
                    balance = round(self.transactions[user_id][other_user.get_id()], 2)
                    if balance > 0:
                        print(f"{other_user.get_name()} owes {user.get_name()}: {balance}")
                        has_balance = True
            if not has_balance:
                print("No balances")

    def add_expense(self, expense_type, amount, user_ids, payer_id, details=None):
        # Convert user IDs to user objects
        users = [self.user_map[user_id] for user_id in user_ids]
        payer = self.user_map[payer_id]
        
        split = None
        if expense_type == 'EQUAL':
            split = EqualSplit()
        elif expense_type == 'PERCENT':
            split = PercentSplit()
        elif expense_type == 'EXACT':
            split = ExactSplit()
        
        if split:
            split.operation(amount, users, payer, details, self)

# Main execution
wallet = Wallet()

# Test commands
wallet.show()
wallet.show('u1')
wallet.add_expense('EQUAL', 1000, ['u1', 'u2', 'u3', 'u4'], 'u1')
wallet.show('u4')
wallet.show('u1')
wallet.add_expense('EXACT', 1250, ['u2', 'u3'], 'u1', [370, 880])
wallet.show()
wallet.add_expense('PERCENT', 1200, ['u1', 'u2', 'u3', 'u4'], 'u4', [40, 20, 20, 20])
wallet.show('u1')
wallet.show()
