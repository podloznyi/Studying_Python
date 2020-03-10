# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
# Выведите показатель степени и саму степень.
# Операцией возведения в степень, а так же функцией возведения в степень пользоваться НЕЛЬЗЯ!

value = int(input('Please enter the value: '))
value = abs(value)
max_value = 1
counter = 0

while max_value < value:
    max_value = max_value * 2
    if max_value > value:
        break
    counter += 1
if value == 1:
    max_value = 1
elif value // 10:
    max_value = max_value // 2
elif not value // 2:
    max_value = max_value // 2
elif value % 2:
    max_value = max_value // 2
print(value, '        ', counter, ' ', max_value)