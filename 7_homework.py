my_dict = {"name": "Vlad", "age": 24, "country": "Russia"}
print(str(my_dict))
print("\n"+("_"*50)+"\n")

#Вывод значений по существующему и отсутствующим ключам.
print("Вывод значения по ключу \"name\":", my_dict["name"])
my_dict["city"] = "Ivanovo"
print("Вывод значения по несуществующему ключу:", my_dict["city"])
print("\n"+("_"*50)+"\n")

#Добавляем ещё 2 пары ключей.
my_dict.update({"street": "Kolotuskina", "house": "42"})


#Удалим одну пару ключ\значение и выведем её на экран.
a = my_dict.pop("name")
print(f"Удаление пары по ключу \"name\": {a}")
print(my_dict)

'''
3. Теперь работаем со множествами.
'''
print("\n"+("_"*50)+"\n")
my_set = {1, 1, 1, True, False, 0, "GET", (1, 2, 3)}
print(my_set)

#Добавим что-нибудь.
my_set.add("POKEMON")
my_set.add(13)
print(my_set)

#И что-нибудь удалим.
my_set.pop()
print(my_set)
