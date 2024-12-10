from typing import List, Dict, Optional
from collections import defaultdict

class SlotType:
    TRUCK = "TRUCK"
    BIKE = "BIKE"
    CAR = "CAR"

class Vehicle:
    def __init__(self, vehicle_type: str, registration_number: str, color: str):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.color = color

class ParkingSlot:
    def __init__(self, slot_type: str, slot_number: int):
        self.slot_type = slot_type
        self.slot_number = slot_number
        self.vehicle: Optional[Vehicle] = None

    def is_free(self) -> bool:
        return self.vehicle is None

    def park_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def unpark_vehicle(self):
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

class Floor:
    def __init__(self, floor_number: int, no_of_slots: int):
        self.floor_number = floor_number
        self.slots: List[ParkingSlot] = []
        self.initialize_slots(no_of_slots)

    def initialize_slots(self, no_of_slots: int):
        # Slot assignment logic: 1 truck, 2 bikes, rest cars
        for i in range(1, no_of_slots + 1):
            if i == 1:
                self.slots.append(ParkingSlot(SlotType.TRUCK, i))
            elif 2 <= i <= 3:
                self.slots.append(ParkingSlot(SlotType.BIKE, i))
            else:
                self.slots.append(ParkingSlot(SlotType.CAR, i))

    def get_free_slots(self, slot_type: str) -> List[int]:
        return [slot.slot_number for slot in self.slots if slot.slot_type == slot_type and slot.is_free()]

    def get_occupied_slots(self, slot_type: str) -> List[int]:
        return [slot.slot_number for slot in self.slots if slot.slot_type == slot_type and not slot.is_free()]

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingSlot]:
        for slot in self.slots:
            if slot.is_free() and slot.slot_type == vehicle.vehicle_type:
                slot.park_vehicle(vehicle)
                return slot
        return None

class ParkingLot:
    _instance = None

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("ParkingLot is a singleton!")
        self.floors: Dict[int, Floor] = {}

    def create_parking_lot(self, parking_lot_id: str, no_of_floors: int, no_of_slots_per_floor: int):
        self.parking_lot_id = parking_lot_id
        for i in range(1, no_of_floors + 1):
            self.floors[i] = Floor(i, no_of_slots_per_floor)
        print(f"Created parking lot with {no_of_floors} floors and {no_of_slots_per_floor} slots per floor")

    def park_vehicle(self, vehicle: Vehicle):
        for floor_number, floor in self.floors.items():
            slot = floor.park_vehicle(vehicle)
            if slot:
                ticket_id = f"{self.parking_lot_id}_{floor_number}_{slot.slot_number}"
                print(f"Parked vehicle. Ticket ID: {ticket_id}")
                return ticket_id
        print("Parking Lot Full")
        return None

    def unpark_vehicle(self, ticket_id: str):
        try:
            _, floor_no, slot_no = ticket_id.split("_")
            floor_no = int(floor_no)
            slot_no = int(slot_no)
            if floor_no in self.floors:
                floor = self.floors[floor_no]
                slot = floor.slots[slot_no - 1]
                if not slot.is_free():
                    vehicle = slot.unpark_vehicle()
                    print(f"Unparked vehicle with Registration Number: {vehicle.registration_number} and Color: {vehicle.color}")
                    return
            print("Invalid Ticket")
        except Exception:
            print("Invalid Ticket")

    def display_free_count(self, vehicle_type: str):
        for floor_number, floor in self.floors.items():
            free_slots = floor.get_free_slots(vehicle_type)
            print(f"No. of free slots for {vehicle_type} on Floor {floor_number}: {len(free_slots)}")

    def display_free_slots(self, vehicle_type: str):
        for floor_number, floor in self.floors.items():
            free_slots = floor.get_free_slots(vehicle_type)
            print(f"Free slots for {vehicle_type} on Floor {floor_number}: {','.join(map(str, free_slots))}")

    def display_occupied_slots(self, vehicle_type: str):
        for floor_number, floor in self.floors.items():
            occupied_slots = floor.get_occupied_slots(vehicle_type)
            print(f"Occupied slots for {vehicle_type} on Floor {floor_number}: {','.join(map(str, occupied_slots))}")

def main():
    parking_lot = ParkingLot.get_instance()
    while True:
        command = input().strip().split()
        if not command:
            continue
        action = command[0]

        if action == "create_parking_lot":
            parking_lot_id, no_of_floors, no_of_slots = command[1], int(command[2]), int(command[3])
            parking_lot.create_parking_lot(parking_lot_id, no_of_floors, no_of_slots)
        elif action == "park_vehicle":
            vehicle_type, reg_no, color = command[1], command[2], command[3]
            parking_lot.park_vehicle(Vehicle(vehicle_type, reg_no, color))
        elif action == "unpark_vehicle":
            ticket_id = command[1]
            parking_lot.unpark_vehicle(ticket_id)
        elif action == "display":
            display_type, vehicle_type = command[1], command[2]
            if display_type == "free_count":
                parking_lot.display_free_count(vehicle_type)
            elif display_type == "free_slots":
                parking_lot.display_free_slots(vehicle_type)
            elif display_type == "occupied_slots":
                parking_lot.display_occupied_slots(vehicle_type)
        elif action == "exit":
            break

if __name__ == "__main__":
    main()
