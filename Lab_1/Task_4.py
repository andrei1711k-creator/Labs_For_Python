total = int(input("Введите сумму в рублях (целое число): "))

result = {}
remaining = total


count = remaining // 100
if count > 0:
    result[100] = count
remaining %= 100


count = remaining // 50
if count > 0:
    result[50] = count
remaining %= 50


count = remaining // 10
if count > 0:
    result[10] = count
remaining %= 10


count = remaining // 5
if count > 0:
    result[5] = count
remaining %= 5


count = remaining // 2
if count > 0:
    result[2] = count
remaining %= 2


count = remaining // 1
if count > 0:
    result[1] = count
remaining %= 1

print(f"Сумма для размена: {total} руб.")
if 100 in result:
    print(f"100 руб. купюр: {result[100]}")
if 50 in result:
    print(f"50 руб. купюр: {result[50]}")
if 10 in result:
    print(f"10 руб. купюр: {result[10]}")
if 5 in result:
    print(f"5 руб. монет: {result[5]}")
if 2 in result:
    print(f"2 руб. монет: {result[2]}")
if 1 in result:
    print(f"1 руб. монет: {result[1]}")

