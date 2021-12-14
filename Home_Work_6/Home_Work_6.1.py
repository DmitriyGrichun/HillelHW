import random
list_1 = []
for _ in range(10):
    list_1.append(random.randint(1, 11))
print(list_1)
print(type(list_1))
print('------------------------------------------')
tuple_1 = tuple(list_1)
print(tuple_1)
print(type(tuple_1))