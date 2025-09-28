import turtle   
turtle.Screen().bgcolor("red")

sc = turtle.Screen()
sc.setup(600 , 600)
sc.title("L-1(A-1)")

turtle.turtle = ("welcome to turtle graphics")
board = turtle.Turtle()

for i in range(4): 
    board.forward(100)
    board.right(90)
    turtle.delay(600)
    i = i + 1
       
