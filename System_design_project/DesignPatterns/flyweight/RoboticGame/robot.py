
from abc import abstractclassmethod

class IRobot:

    @abstractclassmethod
    def display(self, x: int, y: int) -> None:
        pass    