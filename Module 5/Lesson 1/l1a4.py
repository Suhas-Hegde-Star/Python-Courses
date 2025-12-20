import time

class MathClass:
    """

    Welcome to Math Class!

    This is a :

    Docstring for Math Classes
    1. odd_even: Check if the number is odd or even
    2. prime_till: Print all prime numbers till the given number
    3. prime: Check if the number is prime
    """


    def __init__(self, a):
        self.a = a

    def odd_even(self):
        if self.a % 2 == 0:
            return "Even"
        else:
            return "Odd"
        
    def prime_till(self):
        for num in range (2, num1+1):
            prime = True
            if num1 <= 1:
                prime = False
                break
            else:
                for i in range (2, num):
                    if num % i == 0:
                        prime = False
            if prime:
                print(prime, num, "is a prime number") 
            else:
                print(prime, num, "is not a prime number")

    def prime(self):
        if self.a <= 1:
            print(self.a, "is not a prime number")
        else:
            for i in range (2, self.a):
                if self.a % i == 0:
                    print(self.a, "is not a prime number")
                    break
            else:
                print(self.a, "is a prime number")

    """
    
    def factorial(self):
        fact = 1
        for i in range(1, self.a + 1):
            fact = fact * i
        return fact
    
    def add_sub_mul_div(self, b):
        addition = self.a + b
        subtraction = self.a - b
        multiplication = self.a * b
        division = self.a / b
        return addition, subtraction, multiplication, division
        
    """
    
num1 = int(input("Enter a number: "))
print("You entered:", num1)

print(MathClass.__doc__)
time.sleep(3)

math_obj = MathClass(num1)
print("The number is:", math_obj.odd_even())
math_obj.prime_till()
math_obj.prime()

