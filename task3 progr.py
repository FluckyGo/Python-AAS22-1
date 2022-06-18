from task3 import compare

s1 = ('гусь', 'хвост', 'лис', 'собака', 'кошка', 'птица', 'дом', 'январь', 'арматура', 'китай')
s2 = str(input('Введи слово: \n'))

for i in s1:
    print(i, compare(i, s2))







