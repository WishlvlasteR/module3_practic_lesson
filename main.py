def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(10)
print_params(b = 25)
print_params(c = [1, 2, 3])
list_ = [3, 'Hi', 3.14]
dict_ = {'a': [3, 2, 1], 'b': {5, 6.6, 'hello'}, 'c': True}
print_params(*list_)
print_params(**dict_)
values_list2 = [54.32, 'Строка']
print_params(*values_list2, 42)
