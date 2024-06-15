a = "Я памятник себе воздвиг нерукотворный."
print(len(a))
# 38

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
summa = first + second
diff = first - second
if diff < 0:
    diff *= -1
print(f"Сумма заданных чисел равна: {summa}\n" + f"Разность заданных чисел равна: {diff}")

first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
third = float(input("Введите третье число: "))
mean = float((first + second + third) / 3)
print(mean)

first_string = "Вторник"
second_string = "Понедельник"
first_string, second_string = second_string, first_string
print(first_string + ",", second_string)

a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))
f = (((a * b) + (a * c)) ** 3) / 2
print(f)
