from robot import IRobot
from robot_dog import RobotDog
from sprites import Spritis
from humanoid_robot import HumanoidRobot

class RoboticFactory:
    __robotic_object_cache = {}

    @staticmethod
    def create_robot(robot_type: str) -> IRobot:

        if robot_type in RoboticFactory.__robotic_object_cache:
            return RoboticFactory.__robotic_object_cache[robot_type]
        
        else:
            if robot_type == "HUMANOID":
                humanoid_sprit: Spritis = Spritis()
                humanoid_object: IRobot = HumanoidRobot(robot_type, humanoid_sprit)
                RoboticFactory.__robotic_object_cache[robot_type] = humanoid_object
                return humanoid_object
            
            elif robot_type == "ROBOTICDOG":
                robotic_sprit: Spritis = Spritis()
                robotic_object: IRobot = RobotDog(robot_type, robotic_sprit)
                RoboticFactory.__robotic_object_cache[robot_type] = robotic_object
                return robotic_object
            
        return None