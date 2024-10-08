# В некоторых командах будет возможно устанавливать цвет с помощью кодов r, g, b
# Сайт который я рекомендую, он не требует никаких настроек или же регистраций:
# https://htmlcolorcodes.com/
# просто выбираете цвет и палитру этого цвета и справа можете выбрать 3 значения нужные для Вас
import turtle 

screen = turtle.Screen()

t = turtle.Turtle()


"""
Эти методы взаимодействуют с нашим курсором
Они являются самыми простыми и легкими методами, они меняют свойство нашего курсора
"""



"""
t.shape() : меняет форму нашего курсора или же возвращает форму, когда не дали аргументов
Всего доступно несколько форм: 
'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
"""
print('t.shape()')
# выводим цвет по умолчанию
print(t.shape()) # вернет "classic",
# превратит курсор в черепаху
t.shape("turtle")
# выводим форму курсора
print(t.shape()) # вернет "turtle"

"""
t.pencolor() : меняет цвет нашего курсора или же возвращает цвет, когда не дали аргументов
"""
print('t.pencolor()')
# выводим цвет по умолчанию
print(t.pencolor()) # вернет "black"
# устанавливаем цвет нашего курсора на красный
t.pencolor("red")
# выводим цвет
print(t.pencolor()) # вернет "red"


"""
t.fillcolor() : меняет цвет заливки или же возвращает цвет заливки, когда не дали аргументов
"""
print('t.fillcolor()')
# выводим цвет по умолчанию
print(t.fillcolor()) # вернет "black"
# устанавливаем цвет заливки на синий
t.fillcolor("blue")
# выводим цвет
print(t.fillcolor()) # вернет "blue"


"""
t.color() : меняет цвет нашего курсора и заливки или же возвращает цвет, когда не дали аргументов
Первое значение - цвет курсора, второе значение - цвет заливки
"""
print('t.color()')
# значение по умолчанию
print(t.color()) # вернет ("black", "black")
# устанавливаем цвет курсора на красный и цвет заливки на синий
t.color("red", "blue")
# выводим цвет
print(t.color()) # вернет ("red", "blue")

"""
t.reset() : очищает наш курсор и заливку и ставит значения по умолчанию 
"""
print('t.reset()')
t.reset()
# значение по умолчанию
print(t.color()) # вернет ("black", "black")

"""
t.speed() : меняет скорость нашего курсора или же возвращает скорость, когда не дали аргументов
"""
print('t.speed()')
# значение по умолчанию
print(t.speed()) # вернет 3
# устанавливаем скорость нашего курсора на 5
t.speed(5)
# выводим скорость
print(t.speed()) # вернет 5

"""
t.pensize() : меняет размер нашего курсора или же возвращает размер, когда не дали аргументов
"""
print('t.pensize()')
# значение по умолчанию
print(t.pensize()) # вернет 1
# устанавливаем размер нашего курсора на 5
t.pensize(5)
# выводим размер
print(t.pensize()) # вернет 5

"""
t.penup() : приостанавливает наш курсор, возвращает False = курсор опущен, True = курсор поднят
Также можно описать, что мы как-бы поднимаем его с бумаги
"""
print('t.penup()')
# вернет False, так как это значение по умолчанию
print(t.penup())
# приостанавливаем наш курсор
t.penup()
# вернет True, так как мы приостановили курсор
print(t.penup())

"""
t.pendown() : возобновляет наш курсор, возвращает False = курсор поднят, True = курсор опущен
Опять таки мы как-бы опускаем его обратно на бумагу
"""
print('t.pendown()')
# вернет True, так как это значение по умолчанию
print(t.pendown())
# возобновляем наш курсор
t.penup()
# вернет False, так как мы возобновили курсор
print(t.pendown())


"""
t.begin_fill() : начинает заливку фигуры, нужно писать перед тем, как фигура будет нарисована
Не может принимать аргументы
"""
print('t.begin_fill()')
# начинаем заливку
t.begin_fill()

"""
t.end_fill() : заканчивает заливку фигуры, нужно писать после t.begin_fill()
Тоже не может принимать аргументы
"""
print('t.end_fill()')
# заканчиваем заливку
t.end_fill()


"""
t.circle(x) : рисует круг, x - радиус
x - обязателен
"""
print('t.circle(x)')
t.circle(50)


"""
t.goto(x, y) : устанавливает наш курсор в точку x, y
x, y - обязателен

также можно использовать t.setpos(x, y) или t.setposition(x, y) вместо t.goto(x, y)
все три метода будут работать одинаково
"""
print('t.goto(x, y)')
t.goto(5, 5)
t.goto(0,0)


"""
t.pos() : возвращает текущую позицию нашего курсора

также можно использовать t.position() вместо t.pos()
"""
print('t.pos()')
# вернет (0.0, 0.0), так как это значение по умолчанию
print(t.pos())
# устанавливаем наш курсор в точку (10, 10)
t.goto(10, 10)
# вернет (10.0, 10.0), так как мы установили наш курсор заранее
print(t.pos())

"""
t.home() : возвращает наш курсор в начальную точку
"""
print('t.home()')
t.home()


"""
t.clear() : очищает экран
"""
print('t.clear()')
t.clear()


"""
t.setheading(x) : устанавливает направление нашего курсора в градусах
также можно использовать t.seth(x) вместо t.setheading(x)
x - обязателен
0 = вправо, 90 = вверх, 180 = вниз, 270 = влево
"""
print('t.setheading(x)')
t.setheading(90)



"""
Эти и другие методы можно посмотреть в документации
https://docs.python.org/3/library/turtle.html
"""

screen.exitonclick()
