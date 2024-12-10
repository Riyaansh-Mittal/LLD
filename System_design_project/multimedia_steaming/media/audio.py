from .interface import IMedia


class Audio(IMedia):
    def __init__(self, filename):
        self.__filename = filename

    def play(self):
        print(f"Play audio : {self.__filename}")