# Сначала создаём функцию.

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_n = []
        matrix.append(list_n)
        for j in range(m):
            list_n.append(value)

# Хочу, чтобы матрица была матрицей, а не строкой.
    for string_ in matrix:
        print(string_)

# Вставлю инпуты, чтобы вводить нужные значения.
# Обозначу диапозон, дабы избавиться от громосских значений.
# Заодно обыграем ошибки ввода.
i = 0
while i < 3:
    print("_" * 70, "\n")
    try:
        n = int(input("Введите число от 1 до 10: "))
    except ValueError:
        print("Вы ввели не число. Попробуйте заново.")
        i = 0
        continue
    if 1 <= n <= 10:
        i += 1
    try:
        m = int(input("Введите число от 1 до 10: "))
    except ValueError:
        print("Вы ввели не число. Попробуйте заново.")
        i = 0
        continue
    if 1 <= m <= 10:
        i += 1
    try:
        value = int(input("Введите число от 0 до 99: "))
    except ValueError:
        print("Вы ввели не число. Попробуйте заново.")
        i = 0
        continue
    if 0 <= value <= 99:
        i += 1
    if i < 3:
        i = 0
        print("Не корректный ввод. попробуйте заново.")
        print("_" * 70, "\n")

get_matrix(n, m, value)
