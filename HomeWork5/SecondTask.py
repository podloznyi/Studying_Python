# 2. Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
# Используйте для решения задачи функцию `count`

s = (input('Please enter the string: '))
counter = s.count(' ') + 1
if s.find(' ') == 0:
    counter -= 1
if s.rfind(' ') == len(s) - 1:
    counter -= 1

print(counter)