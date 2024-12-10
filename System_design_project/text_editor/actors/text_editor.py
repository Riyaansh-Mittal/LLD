from text_editor.actors.text_editor_subject import ITextEditorSubject
from text_editor.observers.text_editor_observer import ITextEditorObserver

class TextEditor(ITextEditorSubject):

    __observer_list: list = list()  #ItextEditorObserver list
    __current_text: str = ""

    def register_observer(self, observer: ITextEditorObserver) -> None:
        self.__observer_list.append(observer)

    def remove_observer(self, observer: ITextEditorObserver) -> None:
        self.__observer_list.remove(observer)

    def notify_observer(self) -> None:
        print(f"Notify observers with data : {self.__current_text}")

    def set_current_text(self, current_text: str) -> None:
        self.__current_text = current_text