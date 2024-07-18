def sumar(data):
    total_sum = 0

    for item in data:
        if isinstance(item, int) or isinstance(item, float):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            nested_sum = sumar(item)
            total_sum += nested_sum
        elif isinstance(item, dict):
            for key, value in item.items():
                nested_sum = sumar([key, value])
                total_sum += nested_sum

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print("Сумма чисел:", sumar(data_structure))