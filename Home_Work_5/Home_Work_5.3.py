import random

LIST_SIZE = 15
RANDOM_NUMBERS_SIZE = 15
numbers_list_1 = []
numbers_list_2 = []
for _ in range(LIST_SIZE):
    numbers_list_1.append(random.randint(1, RANDOM_NUMBERS_SIZE))
for _ in range(LIST_SIZE):
    numbers_list_2.append(random.randint(1, RANDOM_NUMBERS_SIZE))
print(numbers_list_1)
print(numbers_list_2)
numbers_list_res = []
for i in numbers_list_1:
    if i not in numbers_list_2:
        numbers_list_res.append(i)
print("-----------------------------------------")
print(numbers_list_res)

