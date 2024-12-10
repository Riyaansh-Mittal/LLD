from library_management.items.library_item_interface import ILibraryItem

class CD(ILibraryItem):

    def __init__(self, title: str, unique_id: str, value: int, artist: str):
        self.__title = title
        self.__unique_id = unique_id
        self.__value = value
        self.__artist = artist

    def get_title(self) -> str:
        return self.__title

    def get_unique_id(self) -> str:
        return self.__unique_id

    def claculate_late_fee(self, days: int) -> int:
        return days * 20

    def get_value(self) -> int:
        return self.__value