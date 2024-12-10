from configuration_memento import ConfiguarionMemento
from configuration_originator import ConfigurationOriginator

class ConfigurationCareTaker:

    def __init__(self):
        self.history: list = list()

    def add_memento(self, memento: ConfiguarionMemento):
        self.history.append(memento)

    def undo(self) -> ConfiguarionMemento:
        if self.history:
            last_memento: ConfiguarionMemento = self.history[-1]
            self.history.pop()
            return last_memento
        
        return None
