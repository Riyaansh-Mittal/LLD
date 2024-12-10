class Order:

    def __init__(self, order_id,products):
        self.__order_id = order_id
        self.__products = products

    def __str__(self):
        return f"UserAccount [Username: {self.__order_id}, Password: {self.__products}]"