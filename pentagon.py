import turtle

screen = turtle.Screen()
t = turtle.Turtle()

# Рисуем пятиугольник
for i in range(5):
    t.forward(100)
    t.right(72) 

screen.exitonclick()
