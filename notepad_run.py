from notepad_system import Helper09, Solution

def main():
    # Initialize the helper and solution
    helper = Helper09()
    editor = Solution()
    editor.init(helper)

    # Add some characters with styles
    editor.add_character(0, 0, 'H', "Arial", 12, True, False)
    editor.add_character(0, 1, 'e', "Arial", 12, True, False)
    editor.add_character(0, 2, 'l', "Arial", 12, True, False)
    editor.add_character(0, 3, 'l', "Arial", 12, True, False)
    editor.add_character(0, 4, 'o', "Arial", 12, True, False)

    editor.add_character(1, 0, 'W', "Tahoma", 14, False, True)
    editor.add_character(1, 1, 'o', "Tahoma", 14, False, True)
    editor.add_character(1, 2, 'r', "Tahoma", 14, False, True)
    editor.add_character(1, 3, 'l', "Tahoma", 14, False, True)
    editor.add_character(1, 4, 'd', "Tahoma", 14, False, True)

    # Print the rows
    helper.println("Row 0: " + editor.read_line(0))
    helper.println("Row 1: " + editor.read_line(1))

    # Get styles for specific characters
    helper.println("Style of character at (0, 0): " + editor.get_style(0, 0))
    helper.println("Style of character at (1, 4): " + editor.get_style(1, 4))

    # Delete a character
    editor.delete_character(0, 4)
    helper.println("Row 0 after deleting character at (0, 4): " + editor.read_line(0))

    # Add another character to check functionality
    editor.add_character(0, 4, '!', "Verdana", 16, True, True)
    helper.println("Row 0 after adding '!': " + editor.read_line(0))

if __name__ == "__main__":
    main()
