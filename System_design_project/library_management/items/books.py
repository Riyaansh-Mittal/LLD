from library_management.items.library_item_interface import ILibraryItem

class Books(ILibraryItem):

    def __init__(self, title: str, unique_id: str, author: str, value: int):
        self.__title = title
        self.__unique_id = unique_id
        self.__author = author
        self.__value = value

    def get_title(self) -> str:
        return self.__title

    def get_unique_id(self) -> str:
        return self.__unique_id

    def claculate_late_fee(self, days: int) -> int:
        return days * 30

    def get_value(self) -> int:
        return self.__value