from abc import abstractclassmethod

class IProduct:
    
    @abstractclassmethod
    def display_info(self) -> None:
        pass

