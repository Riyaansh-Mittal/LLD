from auction_manager import AuctionManager

class Auction(AuctionManager):
    def __init__(self):
        self.collegues = list()

    def add_bidder(self, bidder):
        self.collegues.append(bidder)

    def place_bid(self, bidder, bid_amount: int):

        for collegue in self.collegues:
            if collegue.get_name() != bidder.get_name():
                collegue.receive_notification(bid_amount)