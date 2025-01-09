import uuid
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from enum import Enum


# 1. Vehicle Class
class Vehicle:
    def __init__(self, vehicle_type, vehicle_id, station_name, price_per_hour):
        self.vehicle_type = vehicle_type
        self.price_per_hour = price_per_hour
        self.vehicle_id = vehicle_id
        self.station_name = station_name
        self.is_available = True

    def __str__(self):
        return f"{self.vehicle_type} ({self.vehicle_id}) - Station: {self.station_name} - ${self.price_per_hour}/hr"


# 2. Station Class
class Station:
    def __init__(self, station_name):
        self.station_name = station_name
        self.vehicles = {}
        self.dynamic_pricing_applied = False  # Track if dynamic pricing is applied

    def onboard_vehicle(self, vehicle):
        if vehicle.vehicle_type not in self.vehicles:
            self.vehicles[vehicle.vehicle_type] = []
        self.vehicles[vehicle.vehicle_type].append(vehicle)

    def get_available_vehicles(self, vehicle_type):
        if vehicle_type in self.vehicles:
            return [v for v in self.vehicles[vehicle_type] if v.is_available]
        return []

    def drop_vehicle(self, vehicle_id):
        for vehicle_type in self.vehicles:
            for vehicle in self.vehicles[vehicle_type]:
                if vehicle.vehicle_id == vehicle_id:
                    vehicle.is_available = True
                    return True
        return False

    def get_booked_percentage(self, vehicle_type):
        total = len(self.vehicles.get(vehicle_type, []))
        booked = len([v for v in self.vehicles.get(vehicle_type, []) if not v.is_available])
        return booked / total if total else 0

    def update_pricing(self, pricing_strategy):
        for vehicle_type in self.vehicles:
            booked_percentage = self.get_booked_percentage(vehicle_type)
            if booked_percentage >= pricing_strategy.demand_threshold:
            # Apply dynamic pricing if not already applied
                if not self.dynamic_pricing_applied:
                    self.dynamic_pricing_applied = True
                    for vehicle in self.vehicles[vehicle_type]:
                        vehicle.price_per_hour *= (1 + pricing_strategy.price_increase)
            else:
            # Reset dynamic pricing if applied and below threshold
                if self.dynamic_pricing_applied:
                    self.dynamic_pricing_applied = False
                    for vehicle in self.vehicles[vehicle_type] :
                        vehicle.price_per_hour /= (1 + pricing_strategy.price_increase)



# 3. Pricing Strategy Class (Abstract Class)
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, vehicle, duration, station, booked_percentage=0):
        pass


# 4. Fixed Pricing Strategy Class
class FixedPricingStrategy(PricingStrategy):
    def calculate_price(self, vehicle, duration, station, booked_percentage=0):
        return vehicle.price_per_hour * duration


# 5. Dynamic Pricing Strategy Class
class DynamicPricingStrategy(PricingStrategy):
    def __init__(self, demand_threshold=0.8, price_increase=0.1):
        self.demand_threshold = demand_threshold
        self.price_increase = price_increase

    def calculate_price(self, vehicle, duration, station, booked_percentage=0):
        base_price = vehicle.price_per_hour * duration
        if station.dynamic_pricing_applied:
            return base_price * (1 + self.price_increase)  # Price updated due to demand
        return base_price


# 6. Booking Manager Class
class BookingManager:
    def __init__(self):
        self.bookings = {}
        self.id = 1

    def book_vehicle(self, user_name, vehicle_type, station, start_slot, end_slot, pricing_strategy):
        available_vehicles = station.get_available_vehicles(vehicle_type)
        if not available_vehicles:
            return "No vehicles available"

        # For simplicity, we take the first available vehicle for booking
        vehicle = available_vehicles[0]
        duration = self.calculate_duration(start_slot, end_slot)

        booked_percentage = station.get_booked_percentage(vehicle_type)

        # Calculate price based on the dynamic pricing strategy
        price = pricing_strategy.calculate_price(vehicle, duration, station, booked_percentage)

        # Create a booking ID and store the booking
        # booking_id = uuid.uuid4().hex
        booking_id = self.id
        self.id+=1
        self.bookings[booking_id] = {
            "user_name": user_name,
            "vehicle": vehicle,
            "start_slot": start_slot,
            "end_slot": end_slot,
            "station": station,
            "price": price
        }

        # Mark the vehicle as booked (not available)
        vehicle.is_available = False

        # Update pricing for the station if needed
        station.update_pricing(pricing_strategy)

        return f"Booked successfully. Booking ID: {booking_id}, Price: ${price}"

    def drop_vehicle(self, booking_id, station):
        if booking_id not in self.bookings:
            return "Booking ID not found"

        booking = self.bookings[booking_id]
        if booking["station"].station_name != station.station_name:
            return "Vehicle must be dropped at the same station"

        # Mark the vehicle as available
        if booking["vehicle"].is_available == False:
            booking["vehicle"].is_available = True
            del self.bookings[booking_id]
            booked_percentage = station.get_booked_percentage(booking["vehicle"].vehicle_type)
            # Update pricing for the station if needed
            station.update_pricing(pricing_strategy)
        return "Vehicle dropped successfully"

    def calculate_duration(self, start_slot, end_slot):
        # Simplifying: assume start_slot and end_slot are datetime objects
        duration = (end_slot - start_slot).seconds / 3600  # in hours
        return duration


# 7. Station Report Class
class StationReport:
    def __init__(self, station):
        self.station = station

    def generate_report(self):
        report = {"station": self.station.station_name, "vehicles": {}}
        for vehicle_type, vehicles in self.station.vehicles.items():
            booked = sum(1 for v in vehicles if not v.is_available)
            available = len(vehicles) - booked
            report["vehicles"][vehicle_type] = {"available": available, "booked": booked}
        return report


# Enum for Vehicle Types
class VehicleType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    SUV = "SUV"


# Helper Functions for User Interaction
station_registry = {}
booking_manager = BookingManager()
pricing_strategy = DynamicPricingStrategy()  # Using DynamicPricingStrategy


def onboard_station(station_name):
    station = Station(station_name)
    station_registry[station_name] = station
    return f"Station '{station_name}' onboarded."


def onboard_vehicle(station_name, vehicle_type, price_per_hour):
    if station_name not in station_registry:
        return "Station not found."
    
    station = station_registry[station_name]
    vehicle_id = uuid.uuid4().hex
    vehicle = Vehicle(vehicle_type, vehicle_id, station_name, price_per_hour)
    station.onboard_vehicle(vehicle)
    return f"Vehicle {vehicle_type} onboarded at {station_name}."


def search_vehicle(vehicle_type):
    available_vehicles = []
    for station in station_registry.values():
        available_vehicles.extend(station.get_available_vehicles(vehicle_type))
    
    if not available_vehicles:
        return "No vehicles available."

    # Sort by station name and price, and show price for each vehicle
    available_vehicles.sort(key=lambda v: (v.station_name, v.price_per_hour))
    return [
        f"{vehicle} - Price: ${vehicle.price_per_hour}/hr"
        for vehicle in available_vehicles
    ]


def book_car(user_name, vehicle_type, station_name, time_slot):
    if station_name not in station_registry:
        return "Station not found."
    
    start_slot, end_slot = parse_time_slot(time_slot)
    station = station_registry[station_name]
    booking_response = booking_manager.book_vehicle(
        user_name, vehicle_type, station, start_slot, end_slot, pricing_strategy
    )
    return booking_response


def drop_car(booking_id, station_name):
    if station_name not in station_registry:
        return "Station not found."
    
    station = station_registry[station_name]
    drop_response = booking_manager.drop_vehicle(booking_id, station)
    return drop_response


def parse_time_slot(time_slot):
    start, end = time_slot.split("-")
    start_slot = datetime.strptime(start, "%H:%M")
    end_slot = datetime.strptime(end, "%H:%M")
    return start_slot, end_slot


# Main Driver to Simulate User Interactions
def main():
    print(onboard_station("Branch1"))
    print(onboard_station("Branch2"))

    print(onboard_vehicle("Branch1", VehicleType.CAR, 20))
    print(onboard_vehicle("Branch1", VehicleType.CAR, 25))
    print(onboard_vehicle("Branch1", VehicleType.CAR, 30))
    print(onboard_vehicle("Branch1", VehicleType.CAR, 35))
    print(onboard_vehicle("Branch1", VehicleType.CAR, 40))

    print(onboard_vehicle("Branch2", VehicleType.CAR, 20))
    print(onboard_vehicle("Branch2", VehicleType.CAR, 25))
    print(onboard_vehicle("Branch2", VehicleType.CAR, 30))
    print(onboard_vehicle("Branch2", VehicleType.CAR, 35))
    print(onboard_vehicle("Branch2", VehicleType.CAR, 40))

    print(book_car("user1", VehicleType.CAR, "Branch1", "10:00-12:00"))
    print(book_car("user2", VehicleType.CAR, "Branch1", "12:00-14:00"))
    print(book_car("user3", VehicleType.CAR, "Branch1", "14:00-16:00"))
    print(book_car("user4", VehicleType.CAR, "Branch1", "16:00-18:00"))

    # Show search results (dynamic pricing for Branch1 after 4 bookings)
    print(search_vehicle(VehicleType.CAR))

    # Show station report after booking 4 cars
    print(StationReport(station_registry["Branch1"]).generate_report())
    print(drop_car(1, "Branch1"))
    print(search_vehicle(VehicleType.CAR))
    print(book_car("user5", VehicleType.CAR, "Branch1", "18:00-21:00"))
    print(search_vehicle(VehicleType.CAR))


if __name__ == "__main__":
    main()
