class Cat:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def info(self):
        print(f"I am a cat.I am known as {self.name}.I am {self.age} years old.")
    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def info(self):
        print(f"I am a dog.I am known as {self.name}.I am {self.age} years old.")
    def make_sound(self):
        print("bark")

c=Cat(5,"Hello Kitty")
d=Dog(12,"Cheemz")
for animal in(c,d):
    animal.make_sound()
    animal.info()