# Напишите программу, которая будет преобразовывать десятичное число в 
# двоичное.

# *Пример:*

# 45 -> 101101
# 3 -> 11
# 2 -> 10

a = int(input('Введите преобразуемое число: '))
f = bin(a)
print(f'Ответ: {f}.')

# или

a = int(input('Введите преобразуемое число: '))
b = ''
while a > 0:
    b = str(a%2) + b
    a = a // 2
print(f'Ответ: {b}.')