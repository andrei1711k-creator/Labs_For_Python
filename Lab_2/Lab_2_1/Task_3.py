def remove(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            del lst[i]
            return

def append(lst, item):
    lst[len(lst):] = [item]

input_numbers = input("Введите числа через пробел: ")
sp_numbers = input_numbers.split()

number_list = []
for number_string in sp_numbers:
    if '.' in number_string:
        append(number_list, float(number_string))
    else:
        append(number_list, int(number_string))

uni_numbers = []
for number in number_list:
    if number not in uni_numbers:
        append(uni_numbers, number)

max_number = uni_numbers[0]
for number in uni_numbers:
    if number > max_number:
        max_number = number


remove(uni_numbers, max_number)

if uni_numbers:
    sec_max_number = uni_numbers[0]
    for number in uni_numbers:
        if number > sec_max_number:
            sec_max_number = number
    print("Второе по величине число:", sec_max_number)
else:
    print("В списке только одно уникальное число")