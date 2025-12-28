class IOstring:

    """
    Docstring for IOstring
 
        |--------|---------------|--------------------------------------|
        | Steps  |   Function    |         Description                  |
        |--------|---------------|--------------------------------------|
        |Step 1  | get_string    |  Take input from the user            |
        |Step 2  | print_string  |  Print the string in capital letters |
        |--------|---------------|--------------------------------------|
    """

    def __init__(self, input_string=''):
        self.input_string = input_string

    def get_string(self):
        self.input_string = input("Enter a string to turn into capital: ")

    def print_string(self):
        print(self.input_string.upper())

print(IOstring.__doc__)
str_obj = IOstring()
str_obj.get_string()
str_obj.print_string()
