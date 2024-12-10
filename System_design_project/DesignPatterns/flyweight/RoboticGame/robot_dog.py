"""  
This is a immutable class
"""

from robot import IRobot
from sprites import Spritis

class RobotDog(IRobot):
    
    def __init__(self, type: str, body: Spritis):
        self.__type = type
        self.__body = body # small 2d bitmap (graphic element)

    def get_type(self) -> str:
        return self.__type
    
    def get_body(self) -> Spritis:
        return self.__body

    def display(self, x: int, y: int):
        pass