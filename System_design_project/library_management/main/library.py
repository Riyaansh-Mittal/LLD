"""  
NOTES :
If the item here is replacable by any object like cd, dvd, books
and still will work fine, it follows liskov's substitution principle

"""

from library_management.items.library_item_interface import ILibraryItem

class Library:

    def __init__(self, items: ILibraryItem):
        self.__items = items

    def calculate_total_value(self):
        """ calculate total value of library items """

        total_value: int = 0
        for item in self.__items:
            total_value += item
        return total_value
