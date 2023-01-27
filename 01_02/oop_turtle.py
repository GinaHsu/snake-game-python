# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 800
HEIGHT = 800
DELAY = 20 # Milliscrends betwwen screen updates

def move_turtle(t, x, y):
    t.forward(x)
    t.right(y)
    screen.update()
    screen.ontimer(move_turtle(t, x, y), DELAY)


# Create a windown screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Turtle Game")
screen.bgcolor('black')
screen.tracer(0) # turn off automatic animation

#create turtle #1 object
turtle_one = turtle.Turtle()
turtle_one.shape('turtle')
turtle_one.color('red')

#create turtle #2 object
turtle_two = turtle.Turtle()
turtle_two.shape('turtle')
turtle_two.color('blue')

#move_turtle(turtle_one, 10, 10)
move_turtle(turtle_two, -1, -1)

turtle.done()
