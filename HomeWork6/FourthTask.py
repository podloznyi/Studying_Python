height = int(input('\nPlease enter the height of figure:\t'))
print()
width = (height * 2) - 1

if (height % 2) == 0:
    rows = height // 2
    width = (height * 2) - 1
else:
    height = (height // 2) + 1
    width = (height * 2) - 1

print(' "D"')
for i in range(height):
    for k in range(width):
        if height - 1 - i <= k <= height - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
for i in range(height):
    if i == 0:
        continue
    for k in range(width):
        if i == k or i == width - k - 1 or k == width // 2:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()