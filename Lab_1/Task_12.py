BASE_PRICE = 24.99
FREE_MIN = 60
FREE_SMS = 30
FREE_GB = 1

PRICE_MIN = 0.89
PRICE_SMS = 0.59
PRICE_MB = 0.79
TAX = 0.02

minutes = int(input("Введите количество использованных минут: "))
sms = int(input("Введите количество использованных SMS: "))
gb = int(input("Введите количество использованных гигабайт: "))
mb = int(input("Введите количество использованных мегабайт: "))


total_mb_used = gb * 1024 + mb
free_mb = FREE_GB * 1024

extra_minutes = max(0, minutes - FREE_MIN)
extra_sms = max(0, sms - FREE_SMS)
extra_mb = max(0, total_mb_used - free_mb)

cost_extra_minutes = extra_minutes * PRICE_MIN
cost_extra_sms = extra_sms * PRICE_SMS
cost_extra_mb = extra_mb * PRICE_MB

total= BASE_PRICE + cost_extra_minutes + cost_extra_sms + cost_extra_mb
tax = total * TAX
total_with_tax = total + tax

print(f"Базовая стоимость тарифа: {BASE_PRICE:.2f} руб.")
if extra_minutes > 0:
    print(f"Дополнительные минуты: {extra_minutes} мин = {cost_extra_minutes:.2f} руб.")
if extra_sms > 0:
    print(f"Дополнительные SMS: {extra_sms} шт = {cost_extra_sms:.2f} руб.")
if extra_mb > 0:
    print(f"Дополнительный интернет: {extra_mb} МБ = {cost_extra_mb:.2f} руб.")

print(f"Налог (2%): {tax:.2f} руб.")
print(f"Итого к оплате: {total_with_tax:.2f} руб.")

