# 10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
# параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
# параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
# направление сдвига (по умолчанию влево (False)).

def moving(TheNumForMoving, Sdvigi, Direction):
    if Direction:
        TheNumForMoving = TheNumForMoving * (0.1 ** Sdvigi)
        print(TheNumForMoving)
    else:
        TheNumForMoving = TheNumForMoving * (10 ** Sdvigi)
        print(TheNumForMoving)

moving(2, 4, False)