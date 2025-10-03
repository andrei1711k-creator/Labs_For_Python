
string = input("Введите строку: ")


if string == "":
    res_string = ""
else:
    res_string = ""
    current_char = string[0]
    count = 1


    for i in range(1, len(string)):
        if string[i] == current_char:
            count += 1
        else:

            res_string += current_char + str(count)

            current_char = string[i]
            count = 1


    res_string += current_char + str(count)


print("Сжатая строка:", res_string)
