class ConfiguarionMemento:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    @property
    def get_height(self):
        return self.height
    
    @property
    def get_width(self):
        return self.width
    
    def __repr__(self):
        return f"<{self.height} : {self.width}>"