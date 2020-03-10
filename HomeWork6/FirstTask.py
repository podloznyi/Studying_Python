#В этом задании необходимо использовать вложенные циклы. Больше всего подходит цикл FOR.
# Но если кто-то предпочитает WHILE, то можно использовать и его.

height = input('Please enter the height of the figure: ')
width = int(height) * 2 - 1
for i in range(int(height)):
    print(i, end='\t')
    for j in range(width):

            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

