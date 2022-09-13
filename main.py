from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jarod's Snake Game")

snake = []
x_pos = [0, -20, -40]

for i in range(0, 3):
    snake_piece = Turtle()
    snake_piece.penup()
    snake_piece.shape("square")
    snake_piece.color("white")
    snake_piece.goto(x=x_pos[i], y=0)
    snake.append(snake_piece)









screen.exitonclick()