class Image:
    def __init__(self, filename):
        self.__filename = filename


    def display(self):
        print(f"Display image : {self.__filename}")