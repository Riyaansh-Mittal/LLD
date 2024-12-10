class CharFlyweight:
    def __init__(self, ch, font_name, font_size, is_bold, is_italic):
        self.ch = ch
        self.font_name = font_name
        self.font_size = font_size
        self.is_bold = is_bold
        self.is_italic = is_italic

    def get_char(self):
        return self.ch

    def get_char_and_style(self):
        style = f"{self.ch}-{self.font_name}-{self.font_size}"
        if self.is_bold:
            style += "-b"
        if self.is_italic:
            style += "-i"
        return style


class CharFlyweightFactory:
    def __init__(self):
        self.map = {}

    def create_style(self, ch, font_name, font_size, is_bold, is_italic):
        key = f"{ch}-{font_name}-{font_size}"
        if is_bold:
            key += "-b"
        if is_italic:
            key += "-i"

        if key not in self.map:
            self.map[key] = CharFlyweight(ch, font_name, font_size, is_bold, is_italic)

        return self.map[key]


class TextRow:
    def __init__(self):
        self.data = []

    def add_character(self, ch, column):
        self.data.append(ch)
        current = len(self.data) - 1
        while current > 0 and current > column:
            self.data[current], self.data[current - 1] = self.data[current - 1], self.data[current]
            current -= 1

    def get_flyweight(self, column):
        if column < 0 or column >= len(self.data):
            return None
        return self.data[column]

    def read_line(self):
        return self.data

    def delete_character(self, col):
        if col < 0 or col >= len(self.data):
            return False
        del self.data[col]
        return True


class Solution:
    def __init__(self):
        self.helper = None
        self.factory = CharFlyweightFactory()
        self.rows = []

    def init(self, helper):
        self.helper = helper

    def add_character(self, row, column, ch, font_name, font_size, is_bold, is_italic):
        while row >= len(self.rows):
            self.rows.append(TextRow())

        flyweight = self.factory.create_style(ch, font_name, font_size, is_bold, is_italic)
        self.rows[row].add_character(flyweight, column)

    def get_style(self, row, col):
        if row < 0 or row >= len(self.rows):
            return ""
        flyweight = self.rows[row].get_flyweight(col)
        return "" if flyweight is None else flyweight.get_char_and_style()

    def read_line(self, row):
        if row < 0 or row >= len(self.rows):
            return ""
        flyweights = self.rows[row].read_line()
        return "".join(fw.get_char() for fw in flyweights)

    def delete_character(self, row, col):
        if row < 0 or row >= len(self.rows):
            return False
        return self.rows[row].delete_character(col)


# Example helper class
class Helper09:
    def print(self, s):
        print(s, end="")

    def println(self, s):
        print(s)
