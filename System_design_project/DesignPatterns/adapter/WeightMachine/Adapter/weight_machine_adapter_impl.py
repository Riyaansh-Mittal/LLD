from Adapter.weight_machine_adapter import WeightMachineAdapter
from Adaptee.weight_machine import WeightMachine

class WeightMachineAdapterImpl(WeightMachineAdapter):

    def __init__(self, weight_machine: WeightMachine):
        self.weight_machine = weight_machine

    def get_weight_in_kg(self) -> int:
        weight_in_pound: int = self.weight_machine.get_weight_in_pound()

        # Convert it to kg
        weight_in_kg: int = weight_in_pound * 0.45
        return weight_in_kg