from library_management.main.late_fee_calculatable_interface import ILateFeeCalculatable
from typing import List

class LateFeeCalculator:

    def calculate_total_late_fee(items: List[ILateFeeCalculatable], days: int) -> int:
        total_late_fee: int = 0
        for item in items:
            total_late_fee += item.calculate_late_fee(days)
        return total_late_fee

