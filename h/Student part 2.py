class Student:
    grade = 8
    name = "Kanav"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)

ob = Student()
ob.introduction()
ob.details()