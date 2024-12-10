from command import ICommand
from air_conditionar import AirConditionar

class TurnAcOffCommand(ICommand):

    def __init__(self, ac: AirConditionar):
        self.ac = ac

    def execute(self):
        self.ac.turn_ac_off()

    def undo(self):
        self.ac.turn_ac_on()

