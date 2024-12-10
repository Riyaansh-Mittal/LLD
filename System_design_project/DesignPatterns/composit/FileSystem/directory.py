# Composit object
# has-a relationship with the interface FileSystem

from composit.file_system import FileSystem

class Directory(FileSystem):
    
    def __init__(self, name: str):
        self.directory_name = name
        self.filesystem_list: list = list()

    def add(self, file_system_obj: FileSystem) -> None:
        self.filesystem_list.append(file_system_obj)

    def ls(self) -> None:
        print(f"directory Name {self.directory_name}")

        for file_system_obj in self.filesystem_list:
            file_system_obj.ls()