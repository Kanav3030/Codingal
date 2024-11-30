from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can run,walk and swim")

class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can Bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

H =Human()
H.move()

S =Snake()
S.move()

D =Dog()
D.move()

L =Lion()
L.move()