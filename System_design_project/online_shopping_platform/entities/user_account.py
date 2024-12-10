class UserAccount:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def __str__(self):
        return f"UserAccount [Username: {self.__username}, Password: {self.__password}]"
