#Напишите программу, которая считывает целое число и выводит текст, аналогичный
# приведенному в примере (пробелы важны!). Первая строка содержит следующее значение,
# а втора строка содержит предыдущее значение введёного числа

a = int(input('Please enter an integer number: '))
print('The next number for the number', a ,'is', a+1,'\b.')
print('The previous number for the number', a , 'is', a-1,'\b.')