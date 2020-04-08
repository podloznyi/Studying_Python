height = int(input('\nPlease enter the height of figure:\t'))
print()
width = (height * 2) - 1

print(' "B"')
for i in range(height):
    for k in range(width):
        if height - 1 - i <= k <= height - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()