from robot_factory import RoboticFactory
from robot import IRobot

if __name__ == "__main__":
    humanoid_robot1: IRobot = RoboticFactory.create_robot("HUMANOID")
    humanoid_robot1.display(1,2)

    humanoid_robot: IRobot = RoboticFactory.create_robot("HUMANOID")
    humanoid_robot.display(10,30)

    robot_dog1: IRobot = RoboticFactory.create_robot("ROBOTICDOG")
    robot_dog1.display(2,9)

    robot_dog2: IRobot = RoboticFactory.create_robot("ROBOTICDOG")
    robot_dog2.display(11,19)