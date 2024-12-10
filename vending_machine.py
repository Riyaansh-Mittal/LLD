from abc import ABC, abstractmethod


# State Interface
class State(ABC):
    @abstractmethod
    def handle(self, vending_machine):
        pass


# Idle State
class IdleState(State):
    def handle(self, vending_machine):
        print("Machine is idle. Please select an item.")
        item = input("Enter item name: ").strip()
        if item in vending_machine.inventory and vending_machine.inventory[item] > 0:
            vending_machine.selected_item = item
            vending_machine.change_state(WaitingForMoneyState())
        else:
            print("Item not available. Try another selection.")


# Waiting for Money State
class WaitingForMoneyState(State):
    def handle(self, vending_machine):
        price = vending_machine.prices[vending_machine.selected_item]
        print(f"The price of {vending_machine.selected_item} is {price}. Please insert money.")
        money_inserted = float(input("Enter money: "))
        if money_inserted >= price:
            vending_machine.balance = money_inserted - price
            vending_machine.change_state(DispensingItemState())
        else:
            print("Insufficient money. Transaction cancelled.")
            vending_machine.change_state(IdleState())


# Dispensing Item State
class DispensingItemState(State):
    def handle(self, vending_machine):
        print(f"Dispensing {vending_machine.selected_item}.")
        vending_machine.inventory[vending_machine.selected_item] -= 1
        if vending_machine.balance > 0:
            print(f"Returning change: {vending_machine.balance}")
        vending_machine.balance = 0
        vending_machine.selected_item = None
        vending_machine.change_state(IdleState())


# Vending Machine Class
class VendingMachine:
    def __init__(self):
        self.inventory = {
            "chips": 10,
            "soda": 5,
            "candy": 20
        }
        self.prices = {
            "chips": 1.5,
            "soda": 2.0,
            "candy": 1.0
        }
        self.selected_item = None
        self.balance = 0.0
        self.state = IdleState()  # Initial State

    def change_state(self, new_state):
        self.state = new_state

    def run(self):
        while True:
            self.state.handle(self)


# Main Execution
if __name__ == "__main__":
    vending_machine = VendingMachine()
    try:
        vending_machine.run()
    except KeyboardInterrupt:
        print("\nExiting Vending Machine. Have a nice day!")
