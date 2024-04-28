import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
# Moving Up
screen.onkey(user.move, "Up")

# Generating Cars
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(user) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Detect finish line
    if user.is_at_finish():
        user.go_to_starting_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
