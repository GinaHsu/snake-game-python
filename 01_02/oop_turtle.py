# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 1000
HEIGHT = 1000

# Create a windown screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Turtle Game")
screen.bgcolor('black')

#create turtle #1 object
turtle_one = turtle.Turtle()
turtle_one.shape('turtle')
turtle_one.color('red')

#create turtle #2 object
turtle_two = turtle.Turtle()
turtle_two.shape('turtle')
turtle_two.color('blue')

#turtles movement
turtle_one.forward(100)
turtle_one.right(45)
turtle_one.forward(90)
turtle_one.left(45)
turtle_one.forward(90)

turtle_two.forward(-100)
turtle_two.right(-45)
turtle_two.forward(-90)
turtle_two.left(-45)
turtle_two.forward(-90)

turtle.done()
