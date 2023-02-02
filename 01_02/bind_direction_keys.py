# Import the Turtle Graphics module and random modules
import turtle
import random

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 150 # Milliscrends
FOOD_SIZE = 20

offsets = {
    'up': (0, 20),
    'down': (0, -20),
    'left': (-20, 0),
    'right': (20, 0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction('up'), 'Up')
    screen.onkey(lambda: set_snake_direction('right'), 'Right')
    screen.onkey(lambda: set_snake_direction('down'), 'Down')
    screen.onkey(lambda: set_snake_direction('left'), 'Left')

def set_snake_direction(direction):
    global snake_direction
    if direction == 'up':
        if snake_direction != 'down':
            snake_direction = 'up'
    if direction == 'right':
        if snake_direction != 'left':
            snake_direction = 'right'
    if direction == 'down':
        if snake_direction != 'up':
            snake_direction = 'down'
    if direction == 'left':
        if snake_direction != 'right':
            snake_direction = 'left'

def move_snake():
    snake.clearstamps()
    new_head = snake_segment[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake_segment or new_head[0] < - WIDTH / 2 \
        or new_head[0] > WIDTH / 2 or new_head[1] < - HEIGHT / 2 \
        or new_head[1] > HEIGHT / 2:
        reset()
    else:
        # Add new head to snake body
        snake_segment.append(new_head)

        if not is_food_collison():
            snake_segment.pop(0) # no food no grow snake length

        # Draw snake
        for segment in snake_segment:
            snake.goto(segment[0], segment[1])
            snake.stamp()

        # Refresh screen
        screen.title(f'|| Snake Game | Score: {score} ||')
        screen.update()

        # Rinse and repeat
        turtle.ontimer(move_snake, DELAY)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 # Pythagoras Theorem

    return distance

def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)

    return (x, y)

def is_food_collison():
    global food_pos, score

    distance_with_food = get_distance(snake_segment[-1], food_pos)
    if distance_with_food < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True

    return False

def reset():
    global score, snake_segment, snake_direction, food_pos
    score = 0
    snake_direction = 'up'
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    colors = ['light blue', 'pink', 'black']
    color = random.choices(colors, weights = [1, 1, 1], k = 1)[0]
    screen.bgcolor(color)

    snake_segment = [[0, 0], [20, 0], [40, 0], [60, 0]]
    for segment in snake_segment:
        snake.goto(segment[0], segment[1])
        snake.stamp()

    move_snake()


# Global variables
score = 0
snake_direction = 'up'
food_pos = get_random_food_pos()

# Create a windown screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title(f'|| Snake Game | Score: {score} ||')
screen.bgcolor('pink')
screen.tracer(0) # Turn off automatic animation

#create a snake
snake = turtle.Turtle()
snake.shape('square')
snake.color('green')
snake.penup()

# Create Food
food = turtle.Turtle()
food.shape('circle')
food.shapesize(FOOD_SIZE / 20)
food.color('red')
food.penup()

# Event handlers
screen.listen()
bind_direction_keys()

# Set animation in motion
reset()


# Finsh
turtle.done()
