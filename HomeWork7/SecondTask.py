#Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке,
# так и во втором.- Примечание. Эту задачу на Питоне можно решить в одну строчку.

s = input('Please enter the list of numbers: ')
s2 = input('Please enter the second list of numbers: ')
s = s.split()
s2 = s2.split()
s = set(s)
s2 = set(s2)
print(len(s & s2))

