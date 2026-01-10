from abc import ABC, abstractmethod

class ABCclass(ABC):
    def print(self, message):
        print("Test Passed with Efficiency % :", int(message))

    @abstractmethod
    def task(self):
        print("Abstract Method Called")

class BabyClass(ABCclass):
    def tasks(self):
        print("Concrete Method Called")

obj = BabyClass()
obj.task()
obj.print(100)