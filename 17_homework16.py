def print_params(a=1, b="1", c=True):
    print(a, b, c)


# 2. Распаковка параметров.
values_list = [10, "10", False]
values_dict = {"a":42, "b":"42", "c":42.4}

# 3. Распаковка + отдельные параметры.
values_list_2 = [[1, "1", True], "NeOdin"]

print_params(*values_list_2, 42)

print_params(*values_list)
print_params(**values_dict)