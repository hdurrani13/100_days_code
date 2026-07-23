from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")

timmy.penup()
timmy.goto(-250,250)
timmy.pendown()

timmy.color("red", "blue")
timmy.begin_fill()

for _ in range(4):
    timmy.forward(500)
    timmy.right(90)


# timmy.forward(600)
# timmy.right(90)
# timmy.forward(700)
# timmy.right(90)
# timmy.forward(600)


timmy.end_fill()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.right(90)

# import heroes

# print(heroes.gen())








screen = Screen()
# print(screen.window_width())
# print(screen.window_height())
screen.exitonclick()