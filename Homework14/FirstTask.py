from random import randint
def requiredSort(mat, lst):

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                for k in range(len(mat)):
                    mat[k][j], mat[k][j+1] = mat[k][j+1], mat[k][j]

    for i in range(len(mat[0])):
        if i % 2:
            for k in range(len(mat) - 1):
                for j in range(len(mat) - k - 1):
                    if mat[j][i] > mat[j + 1][i]:
                        mat[j][i], mat[j + 1][i] = mat[j + 1][i], mat[j][i]
        else:
            for k in range(len(mat) - 1):
                for j in range(len(mat) - k - 1):
                    if mat[j][i] < mat[j + 1][i]:
                        mat[j][i], mat[j + 1][i] = mat[j + 1][i], mat[j][i]

    return mat, lst

def printMatAndSum(mat, lst):
    for i in range(len(mat)):
        for k in range(len(mat[i])):
            print('{0:>{1}}'.format(str(mat[i][k]), len(str(lst[k]))), end = ' ')
        print()
    for k in  lst:
        print(k, end = ' ')
    print()

m = int(input('Please enter amount of columns: '))
mat = [[randint(10, 50) for k in range(m)] for i in range(m)]
listOfSums = [sum(lst) for lst in mat]
print("Before sorting\n")
printMatAndSum(mat, listOfSums)
mat, lst = requiredSort(mat, listOfSums)
print("\nAfter sorting\n")
printMatAndSum(mat, listOfSums)