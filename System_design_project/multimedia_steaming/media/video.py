from .interface import IMedia

class Video(IMedia):
    def __init__(self, filename):
        self.__filename = filename

    def play(self):
        print(f"Playing video : {self.__filename}")