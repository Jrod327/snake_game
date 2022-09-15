from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import sys
import time

screen = Screen()


def new_game():
    screen.clear()
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Jarod's Snake Game")
    screen.tracer(0)

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(new_game, "r")
    screen.onkey(sys.exit, "q")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 20:
            snake.extend()
            food.refresh()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for i in snake.segments:
            if i == snake.head:
                pass
            elif snake.head.distance(i) < 1:
                game_is_on = False
                scoreboard.game_over()


new_game()
screen.exitonclick()
