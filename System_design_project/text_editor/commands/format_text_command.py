from text_editor.commands.text_editor_command import ITextEditorCommand
from text_editor.formatters.text_formatting_stretegy import ITextFormattingStrategy
from text_editor.actors.text_editor import TextEditor

class FormatTextCommand(ITextEditorCommand):

    def __init__(self, text_formatting_stretegy: ITextFormattingStrategy, text_editor: TextEditor, text_to_format: str):
        self.__text_formatting_stretegy = text_formatting_stretegy
        self.__text_editor = text_editor
        self.__text_to_format = text_to_format

    def execute(self) -> None:
        print("Formatting the text")
        formatted_text: str = self.__text_formatting_stretegy.format(self.__text_to_format)
        self.__text_editor.set_current_text(formatted_text)