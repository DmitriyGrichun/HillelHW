import random

#1. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и печатает его.

def generate_rand_num():
    print(random.randint(1, 100))
generate_rand_num()

#2. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и возвращает его.

def generate_rand_num():
    result = (random.randint(1, 100))
    return result
value = generate_rand_num()
print(value)

#3. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и печатает слово
# "Хорошо", если это число больше 50 или слово "Плохо" в противоположном случае.

def generate_rand_num():
    gen_ran = random.randint(1, 100)
    if gen_ran >= 50:
        print("good")
    else:
        print("bad")

generate_rand_num()

#4. Написать функцию, которая принимает в качестве параметра строку и печатает ее в верхнем регистре (UPPERCASE).

def receive_str():
    str_1 = str("Enter the word ")
    print(str.upper(str_1))

receive_str()

#5. Написать функцию, которая принимает в качестве параметра строку и возвращает ее в верхнем регистре (UPPERCASE).

def receive_str():
    str_to_up = "ddfgdfgdfgdfglpdfmfdgkmfg"
    return str_to_up.upper()
    print(str_to_up)

receive_str()

#6. Написать функцию, которая принимает в качестве параметра список строк и возвращает их в виде списка строк в верхнем регистре (UPPERCASE).

def get_list_1(list_param):
    list_param = [item.upper() for item in list_param]
    return list_param

list_exemp = ["my name is John", "qwerty"]
value = get_list_1(list_exemp)
print(value)

#7. Написать функцию, которая принимает в качестве параметра число и возвращает список чисел от 1 до заданного числа включительно.

def generate_num(gen_number):
    result = [i for i in range(1, gen_number + 1)]
    print(result)

generate_num(6)

#8. Написать функцию, которая принимает в качестве параметра число и возвращает список квадратов чисел от 1 до заданного числа включительно.

def generate_num(gen_number):
    result = [i * i for i in range(1, gen_number + 1)]
    print(result)

generate_num(5)

#Вариант 2
# result = []
# # for i in range(1, gen_number + 1):
# #     result.append(i*i)

