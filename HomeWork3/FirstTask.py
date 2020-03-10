#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
# Программа получает на вход числа `n` и `k` и должна вывести искомое количество яблок (два числа).

kids = int(input('Please enter amount of kids: '))
apples = int(input('Please enter amount of apples: '))
print('The kids will get ', apples // kids, 'apples and ', apples % kids, 'remains at basket')