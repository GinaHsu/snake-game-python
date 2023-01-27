# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 800
HEIGHT = 800
DELAY = 400 # Milliscrends

def move_snake():
    stamper.clearstamps()
    new_head = snake[-1].copy()
    new_head[0] += 20

    # Add new head to snake body
    snake.append(new_head)

    # Remove last segment of snake
    snake.pop(0)

    # Draw snake
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    # Refresh screen
    screen.update()
    # Rinse and repeat
    turtle.ontimer(move_snake, DELAY)



# Create a windown screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor('black')
screen.tracer(0) # Turn off automatic animation

#create a turtle object
stamper = turtle.Turtle()
stamper.shape('square')
stamper.color('pink')
stamper.penup()

#Create snake
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# Draw snake
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# Set animation in motion
move_snake()




# Game ove
turtle.done()
