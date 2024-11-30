class Parrot :
    species ="Byrd"
    def __init__(self,name,age):
        self.name=name
        self.age=age

woo=Parrot("woo",7)
hoo=Parrot("hoo",3)
print("woo is a {}".format (woo.species))
print("hoo is a {} too".format (hoo.species))
print("{} is {} years old".format (woo.name,woo.age))
print("{} is {} years old".format (hoo.name,hoo.age))