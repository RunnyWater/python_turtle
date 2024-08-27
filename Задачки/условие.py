"""
Новая Команда - t.pos(),
t.pos() : возвращает позицию курсора на экране, тип данных - tuple(x, y)


Когда мы поворачиваем курсор влево или вправо то у нас возникает проблема:
курсор никогда или почти никогда не будет в 1 точке дважды 

Теоретическая проблема:
Мы рисуем фигуру и не знаем как она выглядит
Мы также не знаем сколько нам шагов или циклов потребуется для её рисования

Я прошу вас придумать как решить эту проблему и сделать так, чтобы курсор
остановился, когда пришел в изначальную точку, откуда начал рисовать

Удачи! :)
"""

import turtle

t = turtle.Turtle()

# Замените одинарные кавычки на ваш ответ
# Подсказка: сначала курсор находится в позиции (0,0)
while True:
    t.forward(100)
    t.right(90)

    # Есть два варианта решения этой задачи:
    # 1. Первый вариант, мы сравниваем x и y координату отдельно 
    if ('') and (''):
        break

    # 2. Второй вариант, используя 'list comprehension' или 'Списковое включение'
    if tuple("") == (0, 0):
        break

turtle.done()