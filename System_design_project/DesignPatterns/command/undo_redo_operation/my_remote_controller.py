""" INVOKER """

from command import ICommand 

class MyRemoteController:

    def __init__(self):
        self.ac_command_history: list = list()

    def set_command(self, command: ICommand):
        self.command = command

    def press_button(self):
        self.command.execute()
        self.ac_command_history.append(self.command)

    def undo(self):
        if self.ac_command_history:
            last_command: ICommand = self.ac_command_history.pop()
            last_command.undo()
