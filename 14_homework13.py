# Число в первой вставке - случайное.
import random

key_1 = int(random.randint(3, 20))
print("Число в первом камне:", key_1, "\n")

# Захотелось решить с помощью цикла for.
nums = list(range(1, 20))
password = []
for i in nums:
    count_ = 20
    if i < count_:
        for j in nums:
            if (key_1 % (i + j) == 0) and j < i:
                password.append(str(i) + str(j))
                count_ = j


# Ответ.
print("Пароль:", "".join(password), "\n")

# Попарно читается лучше, но не умещается в строку.
print("Пароль:", *password, "\n")

# Времени затрачено примерно полтора часа.
