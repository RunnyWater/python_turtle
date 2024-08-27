import turtle

screen = turtle.Screen()
t = turtle.Turtle()

# Рисуем звезду
for i in range(5):
    t.forward(100)
    t.left(216)

screen.exitonclick()
