from Adaptee.weight_machine import WeightMachine
from Adaptee.weight_machine_for_babies import WeightMachineForBabies
from Adapter.weight_machine_adapter import WeightMachineAdapter
from Adapter.weight_machine_adapter_impl import WeightMachineAdapterImpl

if __name__ == "__main__":

    weight_machine_for_babies = WeightMachineForBabies()
    weight_machine_adapter: WeightMachineAdapter = WeightMachineAdapterImpl(weight_machine_for_babies)
    print(weight_machine_adapter.get_weight_in_kg())
