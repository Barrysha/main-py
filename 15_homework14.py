'''
Пушкин, между прочим. Используя вторую функцию можно проверить наличие того или иного слова в данном стихотворении.
'''
_list = \
"Я помню чудное мгновенье: \
Передо мной явилась ты, \
Как мимолетное виденье, \
Как гений чистой красоты. \
\
В томленьях грусти безнадежной, \
В тревогах шумной суеты, \
Звучал мне долго голос нежный \
И снились милые черты. \
\
Шли годы. Бурь порыв мятежный \
Рассеял прежние мечты, \
И я забыл твой голос нежный, \
Твои небесные черты. \
\
В глуши, во мраке заточенья \
Тянулись тихо дни мои \
Без божества, без вдохновенья, \
Без слез, без жизни, без любви."

# Превращаем строку в список.
_list = _list.split(" ")

# Переменная для счётчика.
calls = 0

# Непосредственно счётчик.
def count_calls():
    global calls
    calls += 1

# Первая функция.
def string_info(pre_tuple):
    count_calls()

    _len = len(pre_tuple)
    _upper = pre_tuple.upper()
    _lower = pre_tuple.lower()

    _tuple = (_len, _upper, _lower)

    print("\n")
    return _tuple

# Вторая функция.
def is_contains(_list, _str):
    count_calls()

# Не придумал, как решить это лаконичне.
    if _str.lower() in _list:
        return True
    elif _str.lower() + "," in _list:
        return True
    elif _str.lower() + ":" in _list:
        return True
    elif _str.lower() + "." in _list:
        return True
    elif _str.capitalize() in _list:
        return True
    elif _str.capitalize() + ","in _list:
        return True
    else:
        return False


while True:
    print("\n" + 50*"_" + "\n")
    fun = input("К какой фунции обращаемся? (HELP для помощи) ")
    print("\n" + 50*"_" + "\n")

    if fun == "HELP": # Инфоблок.
        print(
            "\"info\" принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.", 2*"\n", "\"contains\" принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует.", 2*"\n", "\"Q\" для выхода из программы.", "\n"
            )
        continue

    elif fun == "info": # Первая функция.
        print(
            string_info(pre_tuple = str(input("Введите что-нибудь: ")))
            )
        continue

    elif fun == "contains": # Вторая функция.
        print(
            is_contains(_list, _str = str(input("Введите искомое слово: "))),
            )
        continue

    elif fun == "Q": # Выйдем из цикла
        print("\n" + 50*"_" + "\n")
        break

    else: # Отработаем некорректные вводы.
        print("Некорректный ввод. Попробуйте ещё раз.")
        continue

# Выводим количество вызовов функций (без учёта функции count_calls)
print(f"Количество вызова функций: {calls}")
print("\n" + 50*"_")

# Времени затрачено почти 3 часа. ох...
