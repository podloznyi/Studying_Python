#В школе решили набрать три новых математических класса. Так как занятия по математике
# у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в
# них новые парты. За каждой партой может сидеть не больше двух учеников.
# Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт
# чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа:
# количество учащихся в каждом из трех классов

firstclass = int(input('Please enter amount of kids in a first class: '))
secondclass = int(input('Please enter amount of kids in a second class: '))
thirdclass = int(input('Please enter amount of kids in a third class: '))
if (firstclass/2) > 0:
    firstclass=firstclass +1
if (secondclass / 2) > 0:
        secondclass = secondclass + 1
if (thirdclass/2) > 0:
    thirdclass=thirdclass +1
print('For the first class they will need', firstclass // 2 ,'desks.')
print('For the second class they will need', secondclass // 2 ,'desks.')
print('For the third class they will need', thirdclass // 2 ,'desks.')