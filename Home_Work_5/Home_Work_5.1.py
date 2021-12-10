import random
from collections import OrderedDict

LIST_SIZE = 15
RANDOM_NUMBERS_SIZE = 15
numbers_list = []
for _ in range(LIST_SIZE):
    numbers_list.append(random.randint(1, RANDOM_NUMBERS_SIZE))
print(numbers_list)
for i in list(numbers_list):
    if numbers_list.count(i) > 1:
        numbers_list.remove(i)
print(numbers_list)

# TODO сделал через set один вариант (но он упорядочивает список)
# LIST_SIZE = 30
# RANDOM_NUMBERS_SIZE = 100
# numbers_list = []
# for _ in range(LIST_SIZE):
#     numbers_list.append(random.randint(1, RANDOM_NUMBERS_SIZE))
# print(numbers_list)
# numbers_list_2 = list(set(numbers_list))
# print(numbers_list_2)

# TODO попробовал OrderedDict (но почему то не получил эфект, чтоб остался первоначальный порядок списка)
# LIST_SIZE = 30
# RANDOM_NUMBERS_SIZE = 100
# numbers_list = []
# for _ in range(LIST_SIZE):
#     numbers_list.append(random.randint(1, RANDOM_NUMBERS_SIZE))
# print(numbers_list)
# numbers_list_2 = numbers_list
# numbers_list_2 = list(set(numbers_list))
# list(OrderedDict.fromkeys(numbers_list_2))
# print(numbers_list_2)

# TODO попробовал dict (но почему то не получил эфект, чтоб остался первоначальный порядок списка)
# LIST_SIZE = 30
# RANDOM_NUMBERS_SIZE = 100
# numbers_list = []
# for _ in range(LIST_SIZE):
#     numbers_list.append(random.randint(1, RANDOM_NUMBERS_SIZE))
# print(numbers_list)
# numbers_list_2 = numbers_list
# numbers_list_2 = list(set(numbers_list))
# list(dict.fromkeys(numbers_list_2))
# print(numbers_list_2)

