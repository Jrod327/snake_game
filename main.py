import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jarod's Snake Game")

snake = []
x_pos = [0, -20, -40]


def move_snake():
    for i in range(len(snake)):
        screen.tracer(25)
        snake[i].forward(2)



for i in range(0, 3):
    snake_piece = Turtle()
    snake_piece.penup()
    snake_piece.shape("square")
    snake_piece.color("white")
    snake_piece.goto(x=x_pos[i], y=0)
    snake.append(snake_piece)
print(snake)

screen.listen()
screen.onkeypress(fun=move_snake, key="w")

#look up tracer method

# TODO 1: Create snake body
# TODO 2: Move the snake
# TODO 3: Create snake food
# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with self







screen.exitonclick()