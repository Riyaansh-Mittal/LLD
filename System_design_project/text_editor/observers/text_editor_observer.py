from abc import abstractclassmethod

class ITextEditorObserver:

    @abstractclassmethod
    def update(self, text: str) -> None:
        pass