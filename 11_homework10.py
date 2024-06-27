my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# не могу понять, почему такое задание с циклом "while"
# for i in my_list:
#     if i >= 0:
#         print(i)
#     elif i == 0:
#         continue
#     else:
#         break

start = 0
while start <= len(my_list):
    if my_list[start] > 0:
        print(my_list[start])
        start += 1
    elif my_list[start] == 0:
        start += 1
        continue
    else:
        break
