from abc import abstractclassmethod
from text_editor.observers.text_editor_observer import ITextEditorObserver

class ITextEditorSubject:
    
    # Regester the observer
    @abstractclassmethod
    def register_observer(self, observer: ITextEditorObserver) -> None:
        pass

    # Remove the observer
    @abstractclassmethod
    def remove_observer(self, observer: ITextEditorObserver) -> None:
        pass

    # Notify the observer
    @abstractclassmethod
    def notify_observer(self) -> None:
        pass
    
