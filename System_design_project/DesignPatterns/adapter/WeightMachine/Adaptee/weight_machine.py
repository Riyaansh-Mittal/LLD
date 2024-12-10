from abc import ABC, abstractclassmethod

class WeightMachine(ABC):
    
    @abstractclassmethod
    def get_weight_in_pound(self):
        pass