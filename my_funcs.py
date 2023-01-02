'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
 стоящих на нечётной позиции.Пример1: [2, 3, 5, 9, 3] -> 12'''
def sum_of_index(numbers):
    sum_of_elements = 0
    for elements in range(len(numbers)):
        if elements % 2 != 0:
            sum_of_elements += numbers[elements]
    return sum_of_elements

'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример2: [2, 3, 4, 5, 6] => [12, 15, 16];
            [2, 3, 5, 6] => [12, 15]'''
def Product(numbers):
    prod = 0
    lenght = 0
    result = []
    if len(numbers) % 2 != 0:
        lenght = len(numbers) // 2 + 1
    else:
        lenght = len(numbers) // 2
    for i in range(lenght):
        prod = numbers[i] * numbers[len(numbers) - i - 1]
        result.append(prod)
    return result

'''4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*
- 45 -> 101101
- 3 -> 11
 - 2 -> 10
 '''
def find_binary(num10):
    num2 = ''
    while num10 != 0:
        num2 += str(num10 % 2)
        num10 //= 2
    return num2[::-1]


