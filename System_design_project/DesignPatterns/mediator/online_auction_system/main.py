from auction_manager import AuctionManager
from colleague import Collegue
from bidder import Bidder
from auction import Auction

if __name__ == "__main__":

    auction_manager_obj: AuctionManager = Auction()
    bidder1: Collegue = Bidder("A", auction_manager_obj)
    bidder2: Collegue = Bidder("B", auction_manager_obj)

    bidder1.place_bid(bid_amount=2000)
    bidder2.place_bid(bid_amount=3000)
    bidder1.place_bid(bid_amount=3081)
