# Исходные данные:
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# Ф-ия подсчета суммы эелементов
def calculate_structure_sum(*args):
    total = 0
    for i in args:
        if isinstance(i, (int, float)):
            total += i
        elif isinstance(i, str):
            total += len(i)
        elif isinstance(i, (list, tuple, set)):
            total += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            total += calculate_structure_sum(*i.keys(), *i.values())
    return total


# вывод результата
result = calculate_structure_sum(data_structure)
print(result)
