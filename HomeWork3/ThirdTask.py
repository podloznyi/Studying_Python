#Дано целое, положительное, трёхзначное число. Например: 123, 867, 374.
# Необходимо его перевернуть. Например, если ввели число 123,
# то должно получиться на выходе ЧИСЛО 321. ВАЖНО! Работать только с числами.
# Строки использовать НЕЛЬЗЯ!

number = int(input('Please enter the positive, three digit number: '))
finalnumber = ((number%10)*100) + ((number//10)%10)*10 + (number//100)%10
print('The reverse version of your provided number is ', finalnumber, '\b.')