from online_shopping_platform.entities.user_account import UserAccount

class UserAccountBuilder:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def build(self) -> UserAccount:
        return UserAccount(self.__username, self.__password)
