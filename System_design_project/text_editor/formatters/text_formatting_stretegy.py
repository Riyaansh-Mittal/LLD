from abc import abstractclassmethod

class ITextFormattingStrategy:

    @abstractclassmethod
    def format(self):
        pass