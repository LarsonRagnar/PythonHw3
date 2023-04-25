'''
Задача 16: Требуется вычислить, сколько раз встречается
некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число
N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1


'''
# from random import randint
#
# N = int(input("Введите количество элементов "))
# A = []
# X = randint(0, 10)
# count = 0
# print(f'Число X равно {X}')
# for i in range(N):
#     A.append(randint(0, 10))
# print(A)
# i=0
# while i < len(A):
#     if A[i] == X:
#         count += 1
#         i+=1
#     else:
#         i+=1
# print(f"Число X встречается {count} раз")
'''
import random
my_list=[random.randint(0,10) for _ in range (20)]
print(my_list)
number=int(input('введите искомое число: '))
print(my_list.count(number))
'''
'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5

'''
# from random import randint
#
# import random
#
# my_list = [random.randint(0, 10) for _ in range(20)]
# print(my_list)
# number = int(input('введите искомое число: '))
# count_num = my_list.count(number)
# closest = my_list[0]
# if count_num == 0:
#     for num in my_list:
#         if abs(number - num) < abs(number - closest):
#             closest = num
# print(count_num if count_num > 0 else f'близжайшее к {number} число {closest}')

'''

*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;  очков;  очков; Q, Z – 10 очков. 
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12

'''
points_dict = {'AEIOULNSTRАВЕИНОРСТ': 1,
               'DGДКЛМПУ': 2,
               'BCMPБГЁЬЯ': 3,
               'FHVWYЙЫ': 4,
               'KЖЗХЦЧ': 5,
               'JXШЭЮ': 8,
               'QZФЩЪ': 10}
word = input('Введите слово: ')
score=0
for letter in word.upper():
    for letters in points_dict:
        if letter in letters:
            score += points_dict.get(letters)
print(f'Слово "{word}" стоит  {score} очков')



