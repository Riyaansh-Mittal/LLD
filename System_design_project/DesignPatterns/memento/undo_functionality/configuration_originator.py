from configuration_memento import ConfiguarionMemento

class ConfigurationOriginator:

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def create_memento(self) -> ConfiguarionMemento:
        return ConfiguarionMemento(height=self.height, width=self.width)
    
    def restore_memento(self, memento_restored: ConfiguarionMemento):
        self.height = memento_restored.height
        self.width = memento_restored.width