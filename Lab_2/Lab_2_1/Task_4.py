def count(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

def append(lst, item):
    lst[len(lst):] = [item]

numbers_input = input("Введите числа через пробел: ")
sp_numbers = numbers_input.split()

number_list = []
for number_string in sp_numbers:
    if '.' in number_string:
        append(number_list, float(number_string))
    else:
        append(number_list, int(number_string))

# Уникальные числа
un_numbers = []
for number in number_list:
    if count(number_list, number) == 1:
        append(un_numbers, number)
print("Уникальные числа:", un_numbers)

# Повторяющиеся числа
rep_numbers = []
for number in number_list:
    if count(number_list, number) > 1 and number not in rep_numbers:
        append(rep_numbers, number)
print("Повторяющиеся числа:", rep_numbers)

# Четные числа
chet_numbers = []
for number in number_list:
    if isinstance(number, int):
        if number % 2 == 0:
            append(chet_numbers, number)
print("Четные числа:", chet_numbers)

# Нечетные числа
ne_chet_numbers = []
for number in number_list:
    if isinstance(number, int):
        if number % 2 != 0:
            append(ne_chet_numbers, number)
print("Нечетные числа:", ne_chet_numbers)

# Отрицательные числа
negative_numbers = []
for number in number_list:
    if number < 0:
        append(negative_numbers, number)
print("Отрицательные числа:", negative_numbers)

# Числа с плавающей точкой
float_numbers = []
for number in number_list:
    if isinstance(number, float):
        append(float_numbers, number)
print("Числа с плавающей точкой:", float_numbers)

# Сумма чисел, кратных 5
sum_of_five = 0
for number in number_list:
    if isinstance(number, int):
        if number % 5 == 0:
            sum_of_five += number
print("Сумма чисел, кратных 5:", sum_of_five)

# Максимальное число
max_number = number_list[0]
for number in number_list:
    if number > max_number:
        max_number = number
print("Самое большое число:", max_number)

# Минимальное число
min_number = number_list[0]
for number in number_list:
    if number < min_number:
        min_number = number
print("Самое маленькое число:", min_number)