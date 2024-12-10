from composit.file_system import FileSystem

class File(FileSystem):

    def __init__(self, name: str):
        self.file_name = name

    def ls(self) -> None:
        print(f"File name {self.file_name}")