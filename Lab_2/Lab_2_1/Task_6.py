def append(lst, item):
    lst[len(lst):] = [item]

list_input = input("Введите элементы списка через пробел: ")
sp_list = list_input.split()

unique_list = []

for element in sp_list:
    if element not in unique_list:
        append(unique_list, element)

print("Список без дубликатов:", unique_list)