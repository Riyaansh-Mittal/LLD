"""  
NOTES : 
Current interface is following SINGLE RESPONSIBILITY PRINCLIPLE
If we take claculate_late_fee out, it will make the interface thin which is called
Interface segregation principle
"""

from abc import abstractmethod
from library_management.main.late_fee_calculatable_interface import ILateFeeCalculatable

class ILibraryItem(ILateFeeCalculatable):

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_unique_id(self) -> str:
        pass

    @abstractmethod
    def claculate_late_fee(self) -> int:
        pass

    @abstractmethod
    def get_value(self) -> int:
        pass