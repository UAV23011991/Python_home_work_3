# Задайте рандомно список из чисел размером N, где N число с 
# клавиатуры. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.

# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

N = int(input('Введите N - размер списка: '))
list = []
sum = 0
for i in range(N):
     list_N = int(input(f'Введите число {i+1}:'))
     list.append(list_N)
     if i % 2 != 0:
         sum += list[i]


print(f'Заданный пользователем список: {list}.')
print(f'Сумма нечетных чисел равна: {sum}.')
