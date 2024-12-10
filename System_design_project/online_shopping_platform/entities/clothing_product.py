from online_shopping_platform.entities.product_interface import IProduct

class ClothingProduct(IProduct):
    
    def display_info(self) -> None:
        print("This is clothing product")
