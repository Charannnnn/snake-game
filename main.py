import time
from turtle import Screen
from snake import Snake
from  food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

food.spawn_food()



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    #detect food
    if snake.head.distance(food) < 15:
        scoreboard.increaseScore()
        snake.increaseLength()
        food.spawn_food()

    #detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        food.hideturtle()
        scoreboard.endGame()

    #detect snake collision
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.endGame()




screen.exitonclick()
