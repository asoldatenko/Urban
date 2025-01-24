#1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(12, "стул", False)
print_params(423, "стол")
print_params(534)
print_params(b=25)
print_params(c=[1, 2, 3])

#2
values_list = [432, "Ножка", True]
values_dict = {"a": 234, "b": "ручка", "c": False}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [54, "столбец"]
print_params(*values_list_2, 42)
