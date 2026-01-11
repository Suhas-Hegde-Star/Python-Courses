class A():
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "OBJOCT ONE IS VARY VARY SMOOLLER"
        else:
            return "OBJOCT TWO IS VARY VARY SMOOLLER"

    def __add__(self, other):
        return "ARE, BHAYYA! YE NAHI KAR SAKTE HE!\nJust,telllingyou, my hindi is not that good."
    
obj1 = A(5)
obj2 = A(10)
AareBhayya = 5
NahiKarSakteHo = 10

print(obj1 < obj2)
print(obj1 + obj2)

print(NahiKarSakteHo < AareBhayya)
print(NahiKarSakteHo + AareBhayya)