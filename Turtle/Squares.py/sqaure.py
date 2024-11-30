import turtle

turtle.Screen().bgcolor("red")
sc = turtle.Screen()
sc.setup(300,300)

turtle.title("I love drawing")
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()