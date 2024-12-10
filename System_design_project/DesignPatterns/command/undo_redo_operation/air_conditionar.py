""" Receiver """


class AirConditionar:

    def __init__(self):
        self.is_on: bool = False
        self.temperature: int = 0
    
    def turn_ac_off(self):
        self.is_on = True
        print("AC is OFF")

    def turn_ac_on(self):
        self.is_on = False
        print("AC is ON")

    def set_temperature(self, temp: int):
        self.temperature = temp
        print(f"Temperature changes to {self.temperature}")