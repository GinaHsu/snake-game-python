# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 800
HEIGHT = 800

# Create a windown screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Stamping")
screen.bgcolor('black')

#create turtle #1 object
stamper = turtle.Turtle()
stamper.shape('square')
stamper.color('yellow')
stamper.shapesize(50 / 20)
stamper.stamp()
stamper.penup()

stamper.shapesize(10 / 20)
stamper.goto(100, -100)
stamper.stamp()




turtle.done()
