import numpy
from statistics import mean

# 1) Сумма ряда 0 - 88888888

enter = 88888888
x = 0
y = 1
while y <= enter:
    x += y
    y += 1
print('Сумма чисел: ', x)

enter2 = 88888888
c = 0
for i in range(1,enter2+1):
    c = c+i
print('Answer is: ', c)

n = 88888888
v = sum([i for i in range(1,n+1)])
print('Result v:', v)

# 2) Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]

ryad = [3, 4, 56, 100, 2, 2, 3]

ryad_avg = mean(ryad)

numbers_avg = f'Среднее значение: {mean(ryad)}'

print('Среднее значение: ', ryad_avg)
print(round(ryad_avg, 2))
print(numbers_avg)

listnumbers = ryad
print('Average:', numpy.mean(listnumbers))

# 3) Заменить в строке "asdxfghyxyx" все буквы "х" на "у"

line = 'asdxfghyxyx'
line_new = line.replace('x', 'y')
print(line_new)

# 4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], кратных и 3 и 5.

num_list = [3, 4, 56, 100, 15, 2, 20, 30]
mult = 1

for digit in num_list:
    mult *= int(digit)

print('Произведение чисел:', mult)

# 4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30] кратных и 3 и 5.

num_list1 = [3, 4, 56, 100, 15, 2, 20, 30]
mult1 = 1

for digit1 in num_list1:
    if digit1 % 3 == 0 and digit1 % 5 == 0:
        mult1 *= int(digit1)

print('Произведение чисел кратных и 3 и 5: ', mult1)

# 5) Заменить в строке "asdxfghyxyx" все буквы "х" на "у"  без использования дополнительной строки

string_gen = 'asdxfghyxyx'
print(f"Замена х на у {string_gen.replace('x', 'y')}")
