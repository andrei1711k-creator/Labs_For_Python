total = int(input("Введите сумму в рублях (целое число): "))


remaining = total


count = remaining // 100
if count > 0:
    print(f"100 руб. купюр: {count}")
remaining %= 100


count = remaining // 50
if count > 0:
    print(f"50 руб. купюр: {count}")
remaining %= 50


count = remaining // 10
if count > 0:
    print(f"10 руб. купюр: {count}")
remaining %= 10


count = remaining // 5
if count > 0:
    print(f"5 руб. купюр: {count}")
remaining %= 5


count = remaining // 2
if count > 0:
    print(f"2 руб. купюр: {count}")
remaining %= 2


count = remaining // 1
if count > 0:
    print(f"1 руб. купюр: {count}")
remaining %= 1



