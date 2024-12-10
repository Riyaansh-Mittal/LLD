from text_editor.formatters.text_formatting_stretegy import ITextFormattingStrategy

class UpperCaseStretegy(ITextFormattingStrategy):
    
    def format(self, text: str) -> str:
        print("Converting to the upper case")
        return text.upper()