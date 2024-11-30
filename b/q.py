class Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendict = {}

    def displayBooks(self):
        print(f"We have these books here:(self.name)")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("we have updated the database .you can take the book now")

        else:
            print(f"the book is already in the {self.lendict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("the book has been added to the database")

    def returnbook(self,book):
        self.lendict.pop(book)

if __name__=='__main__':

    books=Library(["Harry Potter And The Cursed Child","The marvels","Eternals","Captain Marvel"], "The Great Stan Lee")

    while(True):
        print(f"You have entered {books.name} library .Enter your choice")
        print("1.Display a book")
        print("2.lend a book")
        print("3.add a book")
        print("4.return a book")
        user_choice = input()
        if user_choice not in ["1","2","3","4"]:
            print("please choose a valid option ")
            continue
        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            books.displayBooks()
 
        elif user_choice == 2 :
            book = input("Select the book you want to lend")
            user = input("Enter your name")
            books.lendbook(user,book)

        elif user_choice == 3:
            book = input("write the name of the book you want to add")
            books.addbook(book)

        elif user_choice == 4:
            book = input("write the name of the book you want to return")
            books.returnbook(book)

        print("press enter to continue and shift to exit")
        user_choice2 = ""
        while(user_choice2!="enter" and user_choice2!="shift"):
            user_choice2 = input()
            if user_choice2 == "shift":
                exit()

            elif user_choice2 == "enter":
                continue