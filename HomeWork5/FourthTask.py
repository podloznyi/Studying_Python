#11. Дана строка. Замените в этой строке все появления буквы `h` на букву `H`,
# # кроме первого и последнего вхождения.
s = (input('Please enter the string: '))

first_index = s.find('h')
second_index = s.rfind('h')
if first_index != second_index:
    s = s[:first_index + 1] + s[first_index + 1:second_index].replace('h', 'H') \
    + s[second_index::]

print(s)