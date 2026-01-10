class ReverseYourSrings:
    def __init__(self):
        self.string = input("Enter a string: ")

    def reverse_string(self):
        return self.string[::-1]
    
obj = ReverseYourSrings()
print("Reversed String is:", obj.reverse_string())