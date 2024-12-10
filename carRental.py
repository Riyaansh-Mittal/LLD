from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from enum import Enum


# Singleton Pattern: RentalManager should be a singleton
class RentalManager:
    _instance = None

    @staticmethod
    def get_instance():
        if RentalManager._instance is None:
            RentalManager._instance = RentalManager()
        return RentalManager._instance

    def __init__(self):
        if RentalManager._instance is not None:
            raise Exception("This is a Singleton class.")
        self.cars = []
        self.bookings = []
    
    def add_car(self, car):
        self.cars.append(car)

    def book_car(self, car, customer, start_date, end_date):
        if car.is_available(start_date, end_date):
            booking = Booking(car, customer, start_date, end_date)
            self.bookings.append(booking)
            car.book(start_date, end_date)
            return booking
        return None


# Enum for Car Types
class CarType(Enum):
    SEDAN = "Sedan"
    SUV = "SUV"
    TRUCK = "Truck"


# Abstract Car class: Template for all cars
class Car(ABC):
    def __init__(self, make, model, daily_rate):
        self.make = make
        self.model = model
        self.daily_rate = daily_rate
        self.booked_dates = []

    @abstractmethod
    def get_type(self):
        pass

    def is_available(self, start_date, end_date):
        for booked_start, booked_end in self.booked_dates:
            if (start_date <= booked_end) and (end_date >= booked_start):
                return False
        return True

    def book(self, start_date, end_date):
        self.booked_dates.append((start_date, end_date))


# Concrete Cars
class Sedan(Car):
    def __init__(self, make, model, daily_rate=30):
        super().__init__(make, model, daily_rate)

    def get_type(self):
        return CarType.SEDAN


class SUV(Car):
    def __init__(self, make, model, daily_rate=50):
        super().__init__(make, model, daily_rate)

    def get_type(self):
        return CarType.SUV


class Truck(Car):
    def __init__(self, make, model, daily_rate=70):
        super().__init__(make, model, daily_rate)

    def get_type(self):
        return CarType.TRUCK


# Factory Pattern: Car Factory
class CarFactory:
    @staticmethod
    def create_car(car_type, make, model):
        if car_type == CarType.SEDAN:
            return Sedan(make, model)
        elif car_type == CarType.SUV:
            return SUV(make, model)
        elif car_type == CarType.TRUCK:
            return Truck(make, model)
        else:
            raise ValueError("Unknown Car Type")


# Strategy Pattern: Pricing Strategy Interface
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, car, start_date, end_date):
        pass


# Concrete Pricing Strategies
class RegularPricingStrategy(PricingStrategy):
    def calculate_price(self, car, start_date, end_date):
        days = (end_date - start_date).days
        return car.daily_rate * days


class DiscountPricingStrategy(PricingStrategy):
    def calculate_price(self, car, start_date, end_date):
        days = (end_date - start_date).days
        discount_rate = 0.9  # 10% discount
        return car.daily_rate * days * discount_rate


# Observer Pattern: Observer Interface for Notifications
class BookingObserver(ABC):
    @abstractmethod
    def update(self, booking):
        pass


# Concrete Observer: Email Notification
class EmailNotification(BookingObserver):
    def update(self, booking):
        print(f"Sending Email: Booking confirmed for {booking.car.make} {booking.car.model} from {booking.start_date} to {booking.end_date}")


# Booking class
class Booking:
    def __init__(self, car, customer, start_date, end_date):
        self.car = car
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Booked"
        self.price = self.calculate_price()

    def calculate_price(self):
        pricing_strategy = RegularPricingStrategy()
        return pricing_strategy.calculate_price(self.car, self.start_date, self.end_date)

    def __str__(self):
        return f"Booking {self.car.get_type()} {self.car.make} {self.car.model}: {self.start_date} to {self.end_date} - ${self.price}"


# Customer class
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# Example Usage
if __name__ == "__main__":
    # Create a rental manager instance (Singleton)
    rental_manager = RentalManager.get_instance()

    # Create some cars
    sedan = CarFactory.create_car(CarType.SEDAN, "Toyota", "Corolla")
    suv = CarFactory.create_car(CarType.SUV, "Ford", "Explorer")
    truck = CarFactory.create_car(CarType.TRUCK, "Ram", "1500")

    # Add cars to rental manager
    rental_manager.add_car(sedan)
    rental_manager.add_car(suv)
    rental_manager.add_car(truck)

    # Create a customer
    customer = Customer("John Doe", "john.doe@example.com")

    # Observer Pattern: Set up email notification for booking
    email_observer = EmailNotification()

    # Book a car
    start_date = datetime.today()
    end_date = start_date + timedelta(days=3)
    booking = rental_manager.book_car(sedan, customer, start_date, end_date)

    if booking:
        # Notify observer
        email_observer.update(booking)
        print(f"Booking Successful: {booking}")
    else:
        print("Car is not available for the selected dates.")
