# Importing Libraries
# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmender"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"

print(table)


