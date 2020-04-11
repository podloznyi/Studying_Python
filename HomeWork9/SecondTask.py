# 10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
# параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
# параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
# направление сдвига (по умолчанию влево (False)).

def moving(TheNumForMoving, Sdvigi, Direction):
    TheNumForMoving = str(TheNumForMoving)
    if Direction == 0:
        for i in range(Sdvigi):
            TheNumForMoving = TheNumForMoving[1:] + TheNumForMoving[0]
        return TheNumForMoving
    else:
        for i in range(Sdvigi):
            TheNumForMoving = TheNumForMoving[-1] + TheNumForMoving[:len(TheNumForMoving)-1]
        return TheNumForMoving

print(moving(123456, 2, False))