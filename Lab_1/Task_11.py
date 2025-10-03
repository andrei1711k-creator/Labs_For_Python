day = int(input("Введите день рождения: "))
month = int(input("Введите номер месяца рождения (1-12): "))

if (21 <= day <= 31 and month == 3) or (1 <= day <= 19 and month == 4):
    zodiac = "Овен"
elif (20 <= day <= 30 and month == 4) or (1 <= day <= 20 and month == 5):
    zodiac = "Телец"
elif (21 <= day <= 31 and month == 5) or (1 <= day <= 20 and month == 6):
    zodiac = "Близнецы"
elif (21 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
    zodiac = "Рак"
elif (23 <= day <= 31 and month == 7) or (1 <= day <= 22 and month == 8):
    zodiac = "Лев"
elif (23 <= day <= 31 and month == 8) or (1 <= day <= 22 and month == 9):
    zodiac = "Дева"
elif (23 <= day <= 30 and month == 9) or (1 <= day <= 22 and month == 10):
    zodiac = "Весы"
elif (23 <= day <= 31 and month == 10) or (1 <= day <= 21 and month == 11):
    zodiac = "Скорпион"
elif (22 <= day <= 30 and month == 11) or (1 <= day <= 21 and month == 12):
    zodiac = "Стрелец"
elif (22 <= day <= 31 and month == 12) or (1 <= day <= 19 and month == 1):
    zodiac = "Козерог"
elif (20 <= day <= 31 and month == 1) or (1 <= day <= 18 and month == 2):
    zodiac = "Водолей"
elif (19 <= day <= 29 and month == 2) or (1 <= day <= 20 and month == 3):
    zodiac = "Рыбы"
else:
    zodiac = "Некорректная дата!"

print("Ваш знак зодиака:", zodiac)
