sec = int(input("Введите количество секунд: "))

minutes = sec // 60
sec = sec % 60


print(f"{minutes} минута(ы) {sec} секунд(ы)")
