task_1 = ('''
Задание №1
Дано: 1 число - сторона квадрата. 
Задача: написать программу, которая рассчитает 3 значения: периметр, площадь, диагональ.''')
print(task_1)
side = 3
p = side*4
s = side**2
d = side * (2 ** 0.5)
result = f'''Ответ:
Периметр: {p}
Площадь: {s}
Диагональ: {d}'''
print(result)

task_2 = ('''
Задание №2
Дано: квадратное уравнение ax**2 + bx + c = 0
Условие: дискриминант уравнение >0
Задача: Найти корни квадратного уравнения, округлить до 2х знаков после запятой.''')
print(task_2)
a = 2
b = 10
c = 2
d = b ** 2 - 4 * a * c
x1 = round((-b + (d ** 0.5)) / 2, 2)
x2 = round((-b - (d ** 0.5)) / 2, 2)
result = f'''Ответ:
x1 = {x1}
x2 = {x2}'''
print(result)

task_3 = ('''
Задание №3
Дано: 2 строки.
Задача: Объединить две строки в одну и разделить их пробелом. 
Поменять местами первые два символа первой строки на первые два символа второй строки и наоборот.''')
print(task_3)
string_1 = 'Кот, который'
string_2 = 'гуляет сам по себе'
string_1_new = string_1.replace(string_1[0:2], string_2[0:2])
string_2_new = string_2.replace(string_2[0:2], string_1[0:2])
result = string_1_new + ' ' + string_2_new
print('Результат:', result)

task_4 = (r'''
Задание №4
Дано: абсолютный путь до файла C:\Python\python.exe
Задача: Вывести названия файла без расширения. Вывести название диска. Вывести название корневой папки.
Решение:''')
print(task_4)
path = r'C:\Python\python.exe'
result = path.split('\\')
a = result[2]
b = a.split('.')
c = b[-1]
d = a.replace(f'.{c}', '')
file = d
a = result[0]
b = a.split(':')
drive = b[0]
root = result[1]
result = f'''Название файла без расширения: {file} 
Название диска: {drive}
Название корневой папки: {root}'''
print(result)

task_5 = ('''
Задание №5
Дано: числа a и b
Задача: используя форматирование строк, вывести на экран сумму и произведение "a + b = c", "a * b = c"''')
print(task_5)
a = 5
b = 7
c1 = a + b
c2 = a * b
result = f'''
{a} + {b} = {c1}
{a} * {b} = {c2}'''
print('Ответ:', result)

task_6 = ('''
Задание №6
Дано: строка
Задача: удалить символы, которые имеют нечётные значения индекса заданной строки.
Решение:''')
print(task_6)
string = 'Кот, который гуляет сам по себе'
result = string[1::2]
print(result)

task_7 = ('''
Задание №7
Дано: 2 строки из неповторяющихся символов. Первая строка длиной 3 символа. Вторая точно содержит символы первой строки
в любом порядке. 
Задача: Найти срез минимальной длины во второй строке, который будет содержать все символы первой строки.''')

print(task_7)
string_1 = 'Кот'
string_2 = 'Труд делает из обезьяны человека'
string_1 = string_1.lower()
string_2 = string_2.lower()
r1 = string_2.find(string_1[0])
r2 = string_2.find(string_1[1])
r3 = string_2.find(string_1[2])
max_len = max(r1, r2, r3)
min_len = min(r1, r2, r3)
result = string_2[min_len:max_len + 1]
print('Ответ: ' + result)
