# Частые live-кодинг задачи
# на собеседовании
#Задача 1 - Найти среднее количество символов в словах строки
based_string = input("Введите строку: ").split()  # Принимает ввод от пользователя и разбивает его на список слов.

result = []  # Инициализирует пустой список для сохранения длин слов.

for i in based_string:
    result.append(len(i))  # Добавляет длину каждого слова в список result.
if len(result) > 0:  # Проверяет, что список не пустой, чтобы избежать деления на ноль.
    print(sum(result) / len(result))  # Выводит среднее количество символов в словах.
else:
    print("Строка была пустой.")  # Сообщает пользователю, если строка не содержала слов.



#Задача 2 - Написать пример декоратора
# Определяем декоратор, который принимает функцию в качестве параметра.
def decorator(function_to_decoration):
    # Определяем внутреннюю функцию-обертку, которая будет обертывать оригинальную функцию.
    def wrapper():
        print("START")  # Выводит сообщение перед вызовом оригинальной функции, указывая на начало декорированного действия.
        function_to_decoration()  # Вызывает оригинальную функцию.
        print("END")  # Выводит сообщение после вызова оригинальной функции, указывая на конец декорированного действия.
    return wrapper  # Возвращает функцию-обертку, чтобы она могла быть использована вместо оригинальной.

# Применяем декоратор к определению функции 'work'.
# Это автоматически обернет функцию 'work' функцией 'wrapper' из декоратора.
@decorator
def work():
    print("MY FUNCTION")  # Оригинальное тело функции, которое будет выполнено между выводами "START" и "END".

# Вызываем декорированную функцию.
# В результате будет выполнен код внутри функции 'wrapper': сначала напечатается "START",
# затем выполнится тело функции 'work', и в конце напечатается "END".
work()





#Задача 3 - Найти самую длинную строку
# Определяем список строк
my_list = ["hello", "hi", "longestword"]

# Используем функцию max с параметром key, установленным в len, для поиска самой длинной строки в списке
word = max(my_list, key=len)

# Выводим найденную строку
print(word)




#Задача 4 - Нахождения самого частого элемента в списке
### Определение функции для нахождения самого частого элемента в списке
def most_frequent(nums: list):
    # Функция max используется для нахождения элемента, который встречается чаще всего.
    # Ключевая функция 'key=nums.count' означает, что для каждого элемента списка будет вызван метод count,
    # и элемент с наибольшим результатом count будет возвращен как самый частый.
    return max(nums, key=nums.count)

# Определение списка чисел
nums = [1, 4, 5, 6, 7, 1, 6, 6]

# Вызов функции most_frequent для списка nums и вывод самого частого элемента,
# а также количества его появлений в списке.
# Функция nums.count(most_frequent(nums)) вызывается дважды: один раз для определения самого частого элемента
# и второй раз для подсчета его количества в списке.

print(most_frequent(nums), " встречается: ", nums.count(most_frequent(nums)))


________________________________________________________



#Задача 5 - Проверка слова на полиндром
# Получаем строку от пользователя, приводим ее к нижнему регистру и удаляем пробелы с обоих концов
phrase = input("Enter string: ").lower().strip().replace(" ", "")

if phrase[::-1] == phrase:
    print("Palindrome")
else:
    print("Not a palindrome")

#################################################################################################################################################
#################################################################################################################################################

#  Сформируйте последовательность Фибоначчи. это последовательность натуральных чисел,
#  где каждое последующее число является суммой двух предыдущих: 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21
# Python. Fibonacci sequence.


LENGTH = 7


def create_fib_sequence(length=LENGTH):
    lst = [0, 1]
    for i in range(1, length-1):
        lst.append(lst[i-1] + lst[i])
    return lst


res = create_fib_sequence()
print(res)


# Сортировка. Пузырьком. Проходимся по элементам массива и
# попарно сравниваем. Если левый больше правого - меняем местами.

# Задача на сортировку пузырьком (Bubble Sort):

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Проходим по массиву и сравниваем каждую пару соседних элементов
        for j in range(0, n-i-1):
            # Если элементы расположены в неправильном порядке, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Пример использования:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Отсортированный массив:")
for i in range(len(arr)):
    print("%d" % arr[i])

# В общем случае, кортеж (tuple) весит меньше, чем список (list). Причина в том, что
# кортежи в Python являются неизменяемыми, то есть их элементы не могут быть
# изменены после создания кортежа. В результате,
# кортежи могут быть более компактными в памяти,
# чем списки, потому что они не требуют дополнительной
# памяти для хранения информации о возможности изменения элементов.
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print("Размер списка:", sys.getsizeof(my_list), "байт")
print("Размер кортежа:", sys.getsizeof(my_tuple), "байт")
############################################################################################################################################################


import MySQLdb
import sqlite3
import pytest


def connect_database():

    # Установка соединения с базой данных
    connection = sqlite3.connect('test.db')

    print("Соединение с БД установлено")

    # Возвращение соединения с БД
    return connection

################################################################################################################################################################
# Цикл для чисел от 1 до 10 только для четных чисел
for i in range(1, 11):
    if i % 2 == 0:  # Проверка на четность числа
        print(i)
        
################
        
#📍 Быстрый сканер открытых портов (портсканер) 📱

#📍Где применимо?

✔ Проверка безопасности серверов (закрыты ли ненужные порты)
✔ Администрирование локальной сети
✔ Сканирование устройств IoT, роутеров, камер
✔ Предварительный аудит сетевой инфраструктуры
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1):
            print(f"✅ Порт открыт: {port}")
    except:
        pass

def scan_ports(ip, ports):
    print(f"🔍 Сканирование IP: {ip}")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, ip, port)

# 🔹 Пример использования
target_ip = "192.168.1.1"  # IP-адрес роутера, сервера или ПК
port_range = range(20, 1024)  # Порты для сканирования

scan_ports(target_ip, 

