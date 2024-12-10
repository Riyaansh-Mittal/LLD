from abc import abstractclassmethod

class Collegue:
    
    @abstractclassmethod
    def place_bid(self, bid_amount: int):
        pass

    @abstractclassmethod
    def receive_bid_notification(self, bid_amount: int):
        pass

    @abstractclassmethod
    def get_name(self) -> str:
        pass