cars_list = [
    ['Nissan', 'Skyline', '1999', 'R34', '2.6', 'R6'],
    ['Honda', 'NSX', '2005', 'C32', '3.0', 'V6'],
    ['Mercedes-Benz', 'ML63', '2008', 'W164', '6.3' ,'V8'],
    ['Toyota', 'Century', '1999', 'G50', '5.0', 'V12'],
]
new_in = str(input('[+] Введи марку или модель (List):  '))
for id in cars_list:
    if new_in in id:
        print(f'Вот, что я нашел по вашему запросу: {id}')

print('Размер в памяти:', cars_list.__sizeof__())

# + Изменяемый тип данных, небольшой размер в памяти
# - Не возможно точно сказать, что означают данные после марки/модели,
# есть некое представление, но без описания не разобраться.

cars_dict = {
   'Nissan Skyline': ('prod_data: 1999', 'code_chassis: R34', 'engine_capacity: 2.6', 'engine_type: R6'),
   'Honda NSX': ('prod_data: 2005', 'code_chassis: C32', 'engine_capacity: 3.0', 'engine_type: V6'),
   'Mercedes-Benz ML63': ('prod_data: 2008', 'code_chassis: W164', 'engine_capacity: 6.3', 'engine_type: V8'),
   'Toyota Century': ('prod_data: 1999', 'code_chassis: G50', 'engine_capacity: 5.0', 'engine_type: V12')
}

while True:
   x = cars_dict.get(input('[+] Введи марку и модель (Key:Value):  '),'Ничего не найдено. Введите другое значение.')
   print(x)
   break

print('Размер в памяти:', cars_dict.__sizeof__())

# + Возможность организовать удобный поиск по Key:Value, наибольшая читабельность, возможность итерировать по key/value
# для экономии памяти
# - Большой занимаемый объем памяти

cars_set = {
    ('Nissan', 'Skyline', '1999', 'R34', '2.6', 'R6'),
    ('Honda', 'NSX', '2005', 'C32', '3.0', 'V6'),
    ('Mercedes-Benz', 'ML63', '2008', 'W164', '6.3' ,'V8'),
    ('Toyota', 'Century', '1999', 'G50', '5.0', 'V12'),
}
new_in = str(input('[+] Введи марку или модель (Set):  '))
for id in cars_set:
    if new_in in id:
        print(f'Вот, что я нашел по вашему запросу: {id}')


print('Размер в памяти:', cars_set.__sizeof__())

# + Быстрое итерирование, 2-е место по занимаемому месту в памяти, не изменяемый
# - Не возможно точно сказать, что означают данные после марки/модели,
#  есть некое представление, но без описания не разобраться
