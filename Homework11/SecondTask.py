# #2. Дан список из чисел и индекс элемента в списке `k`. Напишите функцию для удаления из списка
# элемент с значением `k`, сдвинув влево все элементы, стоящие правее элемента `k`.
#     - функция получает на вход список и число `k`. Функция сдвигает все необходимые элементы,
#     а после этого удаляет последний элемент списка при помощи метода `pop()` без параметров.
#     - функция должна осуществлять сдвиг непосредственно в списке, не создавая нового.
#     - НЕЛЬЗЯ: использовать метод `pop(k)` с параметром, оператор `del`.
#     - МОЖНО ИСПОЛЬЗОВАТЬ: циклы, оператор `if`, функцию `pop()` без параметров.

def fastswap(lst, k):
    while k != len(lst)-1:
        lst[k],lst[k+1] = lst[k+1], lst[k]
        k+=1
    lst.pop()
    return lst

lst = input('Please enter the list of nums: ').split()
k = int(input('Please enter the k index: '))

print(fastswap(lst, k))