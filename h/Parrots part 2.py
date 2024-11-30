class Parrot:
    def init (self, name, song):
        self.name = name
        self.song = song

    def sing(self, song):
        return "{} sings {} ".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)

woo = Parrot("woo", 11)
print(woo.sing("Happy"))
print(woo.dance())
