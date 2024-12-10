"""  
Here we can create product objects

"""
from online_shopping_platform.entities.clothing_product import ClothingProduct
from online_shopping_platform.entities.electronic_product import ElectronicProduct
from online_shopping_platform.entities.product_interface import IProduct


class ProductFactory:
    
    def create_product(self, category: str) -> IProduct:
        category: str = category.lower()
        if category == "electronics":
            return ElectronicProduct()
        elif category == "clothing":
            return ClothingProduct()
        raise ValueError(f"Invalid category : {category}")
