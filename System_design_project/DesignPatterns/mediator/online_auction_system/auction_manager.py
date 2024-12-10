from abc import abstractclassmethod
from colleague import Collegue

class AuctionManager:
    
    @abstractclassmethod
    def add_bidder(self, bidder: Collegue) -> None:
        pass

    @abstractclassmethod
    def place_order(self, bidder: Collegue, bid_amount: int):
        pass