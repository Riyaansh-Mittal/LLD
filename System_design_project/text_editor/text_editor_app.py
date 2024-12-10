from text_editor.actors.text_editor import TextEditor
from text_editor.observers.text_editor_observer import ITextEditorObserver
from text_editor.observers.text_console_observer import TextConsoleObserver
from text_editor.formatters.text_formatting_stretegy import ITextFormattingStrategy
from text_editor.formatters.lower_case_stretegy import LowerCaseStretegy
from text_editor.formatters.upper_case_stretegy import UpperCaseStretegy
from text_editor.commands.format_text_command import FormatTextCommand
from text_editor.commands.text_editor_command import ITextEditorCommand

class TextEditorApp:
    
    @staticmethod
    def main():
        
        # Need to create a text editor
        text_editor: TextEditor = TextEditor()

        # Text editor observers
        observer: ITextEditorObserver = TextConsoleObserver()

        # Register all the observer with the text editor 
        text_editor.register_observer(observer)

        text_editor.set_current_text("Hello students")

        # Formatters
        upper_case_stretegy: ITextFormattingStrategy = UpperCaseStretegy()

        # Commands to create the text
        command: ITextEditorCommand = FormatTextCommand(
                        upper_case_stretegy, text_editor, "Hello students"
                    )
        
        command.execute()

        text_editor.notify_observer()


if __name__ == "__main__":
    TextEditorApp.main()