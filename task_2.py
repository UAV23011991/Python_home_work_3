# Напишите программу, которая найдёт произведение пар чисел списка 
# (Список создаем как в предыдущем задании). Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

number = int(input('Введите размер списка: '))
list = []
list2 = []

for i in range(number):
     list_number = int(input(f'Введите число {i+1}: '))
     list.append(list_number)

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(f'Заданный пользователем список: {list}.')
print(f'Ответ:{list2}.')