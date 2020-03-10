# 2. Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и
# False иначе.

def is_year_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100)

if is_year_leap(int(input('Please enter the year to check: '))):
    print('True')
else:
    print('False')