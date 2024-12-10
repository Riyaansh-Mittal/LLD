from online_shopping_platform.entities.product_interface import IProduct

class ElectronicProduct(IProduct):
    
    def display_info(self) -> None:
        print("This is electronic product")
