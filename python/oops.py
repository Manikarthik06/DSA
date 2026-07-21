"""4 pillars of oops
1.encapsulation
2.abstraction
3.inheritance
4.polymorphism"""

#ENCAPSULATION (HIDING DATA)
"""class A:
    def __init__(self,name,age,gender):
        self.__name=name#private variable can be accessed inside of same class (__)
        self._age=age#protected variable can be accessed inside of same variable (_)
        self.gender=gender# public variable can be accessed inside class and outside of all classes which defines with no prefix
    def display(self):
        print(self.__name,self._age,self.gender)
    def setAge(self,age):
        return self._age
    def getAge(self):
        return self._age
a1=A("mani",21,"male")
a2=A("hello",22,"other")
a1.setAge(33)
a1.display()"""

#BANK ACC
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def getBalance(self):
        return self.__balance
    @abstractmethod
    def interestscale(self):
        pass
class SavingsAccount(BankAccount):
    def interestscale(self):
        return self.getBalance()*0.05
account=SavingsAccount(1000)
print("Initial balance:", account.getBalance())
account.deposit(500)
print("After deposit:", account.getBalance())
account.withdraw(20)
print("After withdrawal:", account.getBalance())
print("Interest:", account.interestscale())
