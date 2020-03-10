# 3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью
# кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side):
    result = (side*4, side**2, side*(2**(1/2)))
    return result

print(square(int(input('Please enter the side of square: '))))