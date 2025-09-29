text = input("Введите строку: ")

res = (text.replace("a", "")
           .replace("e", "")
           .replace("i", "")
           .replace("o", "")
           .replace("u", "")
           .replace("A", "")
           .replace("E", "")
           .replace("I", "")
           .replace("O", "")
           .replace("U", ""))

print("Исходная строка:", text)
print("Строка без гласных:", res)

