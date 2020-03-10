#3. Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается
# чаще всего. Если таких слов несколько, выведите последнее.Задачу необходимо решить с
# использованием словаря.

a = int(input('Enter the number of strings: '))
l = []
for k in range(a):
    s = input('Enter the string: ')
    l += s.split()
d = dict()
max_value = 0
result = ''
for k in l:
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
for k in d:
    if d[k] >= max_value:
        max_value = d[k]
        result = k

print(result)
