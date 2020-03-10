# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N,
# в порядке возрастания.

value = int(input('Please enter the value: '))
value = abs(value)
natural_row = 1
result = 1
string_for_output = ''

while result < value:
    result = natural_row * natural_row
    if value < result:
        break
    natural_row +=1
    string_for_output = string_for_output + str(result) + ' '
print(str(value), '   ' + string_for_output)
print()