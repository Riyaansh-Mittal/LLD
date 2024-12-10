from online_shopping_platform.dal.user_database import UserDatabase
from online_shopping_platform.entities.product_factory import ProductFactory
from online_shopping_platform.entities.product_interface import IProduct
from online_shopping_platform.entities.user_account_builder import UserAccountBuilder
from online_shopping_platform.entities.user_account import UserAccount
from online_shopping_platform.entities.order_builder import OrderBuilder
from online_shopping_platform.entities.order import Order
from typing import List

class ShopWorldApp:

    @staticmethod
    def main():

        # Create the user database - Singleton
        user_database: UserDatabase = UserDatabase.create_instance()
        product_factory: ProductFactory = ProductFactory()
        electronic_product: IProduct = product_factory.create_product(category="electronics")
        electronic_product.display_info()
        clothing_product: IProduct = product_factory.create_product(category="clothing")
        clothing_product.display_info()

        # Build the user account
        user_builder: UserAccountBuilder = UserAccountBuilder(username="username",password="password")
        user_account: UserAccount = user_builder.build()

        print(user_account)

        products: list = list()
        products.append(electronic_product)
        products.append(clothing_product)

        # Build the order
        order_builder: OrderBuilder = OrderBuilder(order_id="order_id", products=products)
        order: Order = order_builder.build()
        print(order)

if __name__ == "__main__":
    
    ShopWorldApp.main()