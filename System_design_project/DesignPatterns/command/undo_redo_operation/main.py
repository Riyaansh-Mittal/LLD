from air_conditionar import AirConditionar
from my_remote_controller import MyRemoteController
from turn_ac_on_command import TurnAcOnCommand

if __name__ == "__main__":

    # AC Object
    air_consitioner: AirConditionar = AirConditionar()

    # Remote Object
    remote_obj: MyRemoteController = MyRemoteController()

    # Create the command and press the button
    turn_ac_on: TurnAcOnCommand = TurnAcOnCommand(air_consitioner)
    remote_obj.set_command(turn_ac_on)
    remote_obj.press_button()

    # undo the last operation
    remote_obj.undo()
