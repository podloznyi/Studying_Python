# 4. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).

def season(month):
    if month == 12 or month >=1 and month < 3:
        return 'Its Winter!'
    if month >= 3 and month <= 5:
        return 'Its spring!'
    if month >= 6 and month <= 8:
        return 'Its summer!'
    if month >= 9 and month < 12:
        return 'Its autumn!'


print(season(int(input('Please enter the number of month: '))))
