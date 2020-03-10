# Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в
# строке `s` всех символов `ch`.
# Для решения можно использовать только функцию `find`(rfind), операторы  if и while.

s = input('Please enter the string: ')
ch = input('Please enter the character which u want to find:  ')
counter = 0
index = s.find(ch)

while index != -1:
    counter += 1
    if index == len(s) - 1:
        break
    else:
        index = s.find(ch, index + 1)

print(counter)

print()