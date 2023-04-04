from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

Screen = Screen()
Screen.setup(width=600, height=600)
Screen.title("My Snake Game")
Screen.bgcolor('black')
Screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

Screen.update()
Screen.listen()
Screen.onkey(key='Up', fun=snake.up)
Screen.onkey(key='Down', fun=snake.down)
Screen.onkey(key='Right', fun=snake.right)
Screen.onkey(key='Left', fun=snake.left)

game_on = True
while game_on:
    time.sleep(0.1)
    snake.move()
    Screen.update()
    
    # picking food
    if snake.head.distance(food.snack) < 15:
        scoreboard.update_score()
        snake.grow()
        food.relocate()

    # detect collision with wall
    if snake.head.xcor() > 270 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -270:
        scoreboard.game_over()
        game_on = False
    
    # detect collision with snake
    for body_part in snake.body_parts:
        if body_part == snake.head:
            continue
        if snake.head.distance(body_part) < 10:
            scoreboard.game_over()
            game_on = False
            

Screen.exitonclick()