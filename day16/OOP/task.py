# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('DarkGreen')
# timmy.shapesize(2,2,2)

# # Move the damn turlte
# timmy.fd(99)
# timmy.bk(209)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# ------------------------------------------------------------#

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Comapines", ["Apple", "Amazon", "Scotia", "Lantern"])
table.add_column("Applied", ["❌", "✅", "❌", "✅"])

print(table)