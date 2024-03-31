#  Частые live-кодинг задачи
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






#Задача 5 - Проверка слова на полиндром
# Получаем строку от пользователя, приводим ее к нижнему регистру и удаляем пробелы с обоих концов
phrase = input("Enter string: ").lower().strip().replace(" ", "")

if phrase[::-1] == phrase:
    print("Palindrome")
else:
    print("Not a palindrome")



word = 'AVIA'
dict_1 = {
    "AEIOULNSTR": 1,
    "DGV": 2,
    "DCMP": 3,
    "АВЕИНОРСТ": 1,
    "ДКЛМПУ": 2,
    "БГЁЬЯ": 3
}
score = 0

for letter in word:
    for key in dict_1:
        if letter.upper() in key:
            score += dict_1[key]
            break

print("The Scrabble score of the word '{}' according to the standard Scrabble rules: {}".format(word, score))
