#Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

day = int(input('Введите число, обозначающее день недели: '))
if day <= 5:
    print('Будни')
elif 8 > day > 5:
    print('Выходные')
else:
    print('Нет такого дня недели')