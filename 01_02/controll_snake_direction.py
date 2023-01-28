# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 800
HEIGHT = 800
DELAY = 400 # Milliscrends

offsets = {
    'up': (0, 20),
    'down': (0, -20),
    'left': (-20, 0),
    'right': (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != 'down':
        snake_direction = 'up'

def go_right():
    global snake_direction
    if snake_direction != 'left':
        snake_direction = 'right'

def go_down():
    global snake_direction
    if snake_direction != 'up':
        snake_direction = 'down'

def go_left():
    global snake_direction
    if snake_direction != 'right':
        snake_direction = 'left'

def move_snake():
    stamper.clearstamps()
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

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
screen.bgcolor('pink')
screen.tracer(0) # Turn off automatic animation

# Event handlers
screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_right, 'Right')
screen.onkey(go_down, 'Down')
screen.onkey(go_left, 'Left')

#create a turtle object
stamper = turtle.Turtle()
stamper.shape('square')
stamper.color('green')
stamper.penup()

#Create snake
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = 'up'

# Draw snake
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# Set animation in motion
move_snake()


# Game ove
turtle.done()
