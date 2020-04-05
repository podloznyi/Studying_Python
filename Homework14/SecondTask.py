a = open('SecondTaskSource.txt', 'r', encoding='utf-8').readlines()
output = open('SecondTaskResult.txt', 'w', encoding='utf-8')
dict1 = dict()
sum1 = 0
maxlen = 0
for k in range(len(a)):
    a[k] = a[k].split()
    a[k][0] = a[k][0][0] + '.'
    sum = 0
    for i in range(2, len(a[k])):
        sum += int(a[k][i])
    sum = sum/int(len(a[k][2:]))
    sum1 += sum
    print('{0: <{1}}'.format(a[k][1] + ' ' + a[k][0], maxlen),
          '{:.2f}'.format(sum), sep='\t', file=output)
    if sum < 5:
        dict1[a[k][1]+' '+ a[k][0]] = sum
        if maxlen < len(a[k][1]+' '+ a[k][0]):
            maxlen = len(a[k][1]+' '+ a[k][0])

for k in dict1:
    print('{0: <{1}}'.format(k, maxlen), '{:.2f}'.format(dict1[k]), sep='\t')
print('{0: <{1}}'.format('Класс', maxlen), '{:.2f}'.format(sum1 / len(a)),
      sep='\t')
output.close()
