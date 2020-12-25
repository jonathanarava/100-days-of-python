# import another_module
# print(another_module.another_variable)
#
#
# from turtle import Turtle, Screen # import turtle
# timmy = Turtle()  # turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(300)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"  # center aligned bt default

print(table)
