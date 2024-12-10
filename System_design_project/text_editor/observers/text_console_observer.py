from text_editor.observers.text_editor_observer import ITextEditorObserver

class TextConsoleObserver(ITextEditorObserver):

    def update(self, text: str) -> None:
        print(f"Text updated in console : {text}")
