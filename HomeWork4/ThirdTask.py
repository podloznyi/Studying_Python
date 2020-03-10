#Программа запрашивает ввод последовательности целых чисел, пока не будет введён 0. Как только
#будет введён 0 (ноль), программа должна посчитать и вывести на экран:
#- количество введённых чисел (завершающий 0 не считается)
#- их сумму
#- среднее арифметическое (не считая завершающего числа 0)
#- определить максимальное и минимальное значение
#- определить количество чётных и не чётных элементов в последовательности

counter = 0
summary = 0
even = 0
not_even = 0
value = int(input('Please enter the values: '))
min_value = value
max_value = value
average_arithmetic = 0


while value != 0:
    counter += 1
    if value > max_value:
        max_value = value
    summary = summary + value
    if value < min_value:
        min_value = value
    if value % 2 > 0:
        not_even += 1
    if value % 2 == 0:
        even += 1
    value = int(input('Please enter the values: '))
if counter != 0:
    average_arithmetic = summary // counter
print(counter, summary, average_arithmetic,
      max_value, min_value, not_even, even)