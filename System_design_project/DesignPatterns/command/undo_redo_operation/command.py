from abc import abstractclassmethod

class ICommand:

    @abstractclassmethod
    def execute(self):
        pass

    @abstractclassmethod
    def undo(self):
        pass