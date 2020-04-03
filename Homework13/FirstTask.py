from random import randrange
m = int(input('Please enter the M: '))
n = int(input('Please enter the N: '))
matrix = [[randrange(10, 100) for i in range(m)] for k in range(n)]
a = []
for i in range(m):
    sum = 0
    for k in matrix:
        sum+=k[i]
    a.append(sum)
for i in range(n):
    sum = 0
    for k in range(m):
        print('{0: >{1}}'.format(matrix[i][k], len(str(a[k]))), end=' ')
        sum+=matrix[i][k]
    print('    ', sum)
for i in a:
    print(i, end=' ')