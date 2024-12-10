from colleague import Collegue
from auction_manager import AuctionManager

class Bidder(Collegue):

    def __init__(self, name: str, auction_manager: AuctionManager):
        self.name = name
        self.auction_manager = auction_manager
        auction_manager.add_bidder(self)

    def place_bid(self, bid_amount: int):
        self.auction_manager.place_order(self, bid_amount)

    def receive_notification(self, bid_amount: int):
        print(f"Bidder {self.name} got the notification")

    def get_name(self) -> str:
        return self.name