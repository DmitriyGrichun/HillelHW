import random

#1. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и печатает его.

# def generate_rand_num():
#     result = [random.randint(1, 100) for _ in range(1)]
#     print(result)
# generate_rand_num()

#2. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и возвращает его.

# def generate_rand_num():
#     result = [random.randint(1, 100) for _ in range(1)]
#     return result
# value = generate_rand_num()
# print(value)

#3. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и печатает слово
# "Хорошо", если это число больше 50 или слово "Плохо" в противоположном случае.

# def generate_rand_num():
#     result = [random.randint(1, 100) for _ in range(1)]
#     print(result)
#     for i in list(result):
#         if i >= 50:
#             print("good")
#         else:
#             print("bad")
#
# generate_rand_num()

#4. Написать функцию, которая принимает в качестве параметра строку и печатает ее в верхнем регистре (UPPERCASE).

# def receive_str():
#     str_1 = str([input("Enter the word in the lower case ")])
#     print(str.upper(str_1))
#
# receive_str()

#5. Написать функцию, которая принимает в качестве параметра строку и возвращает ее в верхнем регистре (UPPERCASE).

# def receive_str(some_str):
#     return some_str.upper()
#
# str_to_up = "ddfgdfgdfgdfglpdfmfdgkmfg"
# value = receive_str(str_to_up)
# print(value)


#6. Написать функцию, которая принимает в качестве параметра список строк и возвращает их в виде списка строк в верхнем регистре (UPPERCASE).

def get_list_1(list_param):
    new_list_param = " ".join(list_param)
    new_list_param = new_list_param.upper()
    list_param = new_list_param.split(" ")
    return list_param

list_exemp = ["hello", "test", "world"]
value = get_list_1(list_exemp)
print(value)

#7. Написать функцию, которая принимает в качестве параметра число и возвращает список чисел от 1 до заданного числа.
#8. Написать функцию, которая принимает в качестве параметра число и возвращает список квадратов чисел от 1 до заданного числа.
