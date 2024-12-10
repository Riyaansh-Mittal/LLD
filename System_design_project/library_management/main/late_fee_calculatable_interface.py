
from abc import ABCMeta, abstractmethod

class ILateFeeCalculatable(ABCMeta):

    @abstractmethod
    def calculate_late_fee(self, days: int) -> str:
        pass
