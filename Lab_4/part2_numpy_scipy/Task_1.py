import numpy as np


def analyze_tr_ex(expenses):

    expenses= np.array(expenses)

    winter_months = [11, 0, 1]

    summer_months = [5, 6, 7]


    winter_ex = sum(expenses[winter_months])
    summer_ex = sum(expenses[summer_months])
    if winter_ex > summer_ex:
        comp = "Зимой тратится больше"
    elif winter_ex < summer_ex:
        comp = "Летом тратится больше"
    else:
        comp = "Расходы равны"


    max_expense = np.max(expenses)
    max_months = np.where(expenses == max_expense)[0] + 1
    print(f"Расходы зимой: {winter_ex} руб.")
    print(f"Расходы летом: {summer_ex} руб.")
    print(f"Сравнение: {comp}")
    print(f"Месяц(ы) с наибольшим(и) расходами: {max_months}")
    return " "





expenses = [1200, 1300, 1100, 1000, 900, 800, 850, 900, 950, 1000, 1100, 1500]
print(analyze_tr_ex(expenses))