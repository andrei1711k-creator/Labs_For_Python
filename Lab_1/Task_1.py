
surname = input("Введите фамилию : ")

name = input("Введите имя : ")

otchestvo = input("Введите отчество : ")


fio = f"{surname.capitalize()} {name[0].upper()}.{otchestvo[0].upper()}."


print(f"Форматированное ФИО: {fio}")
