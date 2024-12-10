from abc import ABC, abstractclassmethod

class WeightMachineAdapter(ABC):

    @abstractclassmethod
    def get_weight_in_kg(self):
        pass