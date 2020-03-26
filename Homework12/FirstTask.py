# 1. Необходимо написать функцию для проверки корректности пароля. Функция принимает в качестве параметра пароль который необходимо проверить и возвращает True если пароль верный, иначе False.
# Правила которым должен соответствовать пароль:
# 	a. длина пароля должна быть больше или равна 8 символам
# 	b. пароль должен содержать символы латинского алфавита верхнего и нижнего регистров (a - z и  A - Z обязательно должны присутствовать оба регистра)
# 	c. пароль должен содержать цифры от 0 до 9 (минимум 1 символ)
# 	d. пароль должен содержать специальные символы: @ # % & _ (минимум 1 символ)
# Можно использовать функции isnumeric(), isupper(), islower().

def func(password):
     a = False
     b = False
     c = False
     d = False
     setforcheck = ['@', '#', '%', '&', '_']
     for k in password:
          if k.isnumeric():
               a = True
          if k.isupper():
               b = True
          if k.islower():
               c = True
          if k in setforcheck:
               d = True
     return a and b and c and d and len(password) >= 8

print(func('@Ent3rPasswordHere'))