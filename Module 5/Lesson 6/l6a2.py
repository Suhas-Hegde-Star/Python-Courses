class A():
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "OBJOCT ONE IS VARY VARY SMOOLLER"
        else:
            return "OBJOCT TWO IS VARY VARY SMOOLLER"

    def __eq__(self, other):
        if self.a == other.a:
            return "OBJOCT ONE IS EQUAL TO OBJOCT TWO" and "ARE, BHAYYA! YE NAHI KAR SAKTE HE!\nJust,tellling you, my hindi is not that good."
        else:
            return "OBJOCT ONE IS NOT EQUAL TO OBJOCT TWO" and "ARE, BHAYYA! YE NAHI KAR SAKTE HE!\nJust,tellling you, my hindi is not that good."
        

obj1 = A(5)
obj2 = A(10)
obj3 = A(67)
obj4 = A(7)

print(obj1 < obj2)
print(obj3 < obj4)

print(obj1 == obj2)
print(obj3 == obj4)

print("Passed Values:", obj1.a, obj2.a)
print("Passed Values:", obj3.a, obj4.a)