from online_shopping_platform.entities.product_interface import IProduct
from online_shopping_platform.entities.order import Order

from typing import List

class OrderBuilder:
    def __init__(self, order_id: str, products: List[IProduct]):
        self.__order_id = order_id
        self.__products = products

    def build(self) -> Order:
        return Order(self.__order_id, self.__products)