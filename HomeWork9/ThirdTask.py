# 3. Реверс списка
# - Принцип алгоритма заключается в следующем: мы меняем местами 0-ый элемент с последним, 1-ый с
# предпоследним и д.т.
# - Итого количество таких обменов будет равно половине длины списка. Иначе элементы поменяются
# местами по-второму кругу и вернутся в первоначальное положение.

def reverse():
    firstlst = input('Please enter the list objects trow the spaces: ').split()
    length = len(firstlst)
    length2 = length // 2
    for k in range(length2):
        firstlst[k], firstlst[(length-1) - k] = firstlst[(length-1) - k], firstlst[k]
    return firstlst

print(reverse())