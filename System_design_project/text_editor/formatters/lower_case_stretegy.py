from text_editor.formatters.text_formatting_stretegy import ITextFormattingStrategy

class LowerCaseStretegy(ITextFormattingStrategy):
    
    def format(self, text: str) -> str:
        print("Converting to the lower case")
        return text.lower()