from abc import abstractclassmethod

class ITextEditorCommand:

    @abstractclassmethod
    def execute(self):
        pass
