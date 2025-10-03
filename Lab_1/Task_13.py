import random

secret = random.randint(1, 100)
guess = None

print("Угадай число от 1 до 100")

while guess != secret:
    guess = int(input("Введите число: "))
    if guess < secret:
        print("Больше!")
    elif guess > secret:
        print("Меньше!")
    else:
        print("Поздравляю! Вы угадали число!")
