# 9. Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
# Небольшая подсказка. В этой задаче вам понадобится:
#     - список
#     - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не
#     придётся разворачивать
#     список), чтоб развернуть список, метод `join()`
#     - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from
#     string import
#     ascii_uppercase`), она содержит все буквы латинского алфавита.

from string import ascii_uppercase



def converter(value):
    if value > 9:
        return ascii_uppercase[value-10]
    else:
        return str(value)
def translator(value, n):
    reversed_value = []
    result = ''
    if value == 0:
        reversed_value.append(value)
    while value > 0:
        reversed_value.append(value % n)
        value = value // n
    reversed_value.reverse()
    for k in reversed_value:
        result = result + converter(k)
    return result

print(translator(int(input('Please enter the value: ')),
        int(input('Please enter the numeral system: '))))