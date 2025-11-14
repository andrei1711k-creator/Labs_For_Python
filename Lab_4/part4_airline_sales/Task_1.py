import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 6)
pd.set_option('display.max_columns', None)

DATA_PATH = r"C:\Users\User\Downloads\Telegram Desktop\s7_data_sample_rev4_50k.xlsx"
SHEET_NAME = "DATA"
data_set = pd.read_excel(DATA_PATH, SHEET_NAME)

data_set['ISSUE_DATE'] = pd.to_datetime(data_set['ISSUE_DATE'], errors='coerce')
data_set['FLIGHT_DATE_LOC'] = pd.to_datetime(data_set['FLIGHT_DATE_LOC'], errors='coerce')

data_set['issue_month'] = data_set['ISSUE_DATE'].dt.month
data_set['issue_year'] = data_set['ISSUE_DATE'].dt.year
data_set['issue_quarter'] = data_set['ISSUE_DATE'].dt.quarter
data_set['issue_dayofweek'] = data_set['ISSUE_DATE'].dt.dayofweek
data_set['flight_month'] = data_set['FLIGHT_DATE_LOC'].dt.month
data_set['flight_year'] = data_set['FLIGHT_DATE_LOC'].dt.year
data_set['days_before_flight'] = (data_set['FLIGHT_DATE_LOC'] - data_set['ISSUE_DATE']).dt.days

numeric_cols = data_set.select_dtypes(include=[np.number])

plt.figure(figsize=(10, 5))
sns.histplot(data_set["REVENUE_AMOUNT"], bins=50, kde=True)
plt.title("Распределение суммы выручки")
plt.xlabel("Выручка за билет, руб.")
plt.ylabel("Количество продаж")
plt.show()

if "days_before_flight" in data_set.columns:
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x="days_before_flight", y="REVENUE_AMOUNT", data=data_set, alpha=0.3)
    plt.title("Связь между временем покупки и выручкой")
    plt.xlabel("Дней до вылета")
    plt.ylabel("Выручка за билет")
    plt.show()

weekday_sales = data_set.groupby("issue_dayofweek")["REVENUE_AMOUNT"].agg(["mean", "sum", "count"])
weekday_sales.index = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

plt.figure(figsize=(10, 5))
sns.barplot(x=weekday_sales.index, y=weekday_sales["mean"])
plt.title("Средняя выручка по дням недели покупки")
plt.xlabel("День недели")
plt.ylabel("Средняя выручка, руб.")
plt.show()

monthly_revenue = data_set.groupby("issue_month")["REVENUE_AMOUNT"].agg(["mean", "sum", "count"])
months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
monthly_revenue = monthly_revenue.reset_index()
monthly_revenue['Месяц'] = monthly_revenue['issue_month'].apply(lambda x: months[x - 1])
monthly_revenue = monthly_revenue[['Месяц', 'mean', 'count', 'sum']].rename(columns={
    'mean': 'Средняя_стоимость_билета_руб',
    'count': 'Количество_продаж',
    'sum': 'Общая_выручка_руб'
})

plt.figure(figsize=(15, 8))

plt.subplot(2, 1, 1)
bars = plt.bar(monthly_revenue['Месяц'], monthly_revenue['Средняя_стоимость_билета_руб'], color='skyblue', alpha=0.7)
plt.title('Средняя стоимость билета по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Средняя стоимость билета, руб.')
plt.grid(True, alpha=0.3)

for bar, value in zip(bars, monthly_revenue['Средняя_стоимость_билета_руб']):
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + monthly_revenue['Средняя_стоимость_билета_руб'].max() * 0.01,
             f'{value:.0f} руб.', ha='center', va='bottom', fontsize=9)

plt.subplot(2, 1, 2)
plt.plot(monthly_revenue['Месяц'], monthly_revenue['Количество_продаж'], color='red', marker='o', linewidth=2,
         markersize=6)
plt.title('Количество продаж по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество проданных билетов')
plt.grid(True, alpha=0.3)

for i, (month, count) in enumerate(zip(monthly_revenue['Месяц'], monthly_revenue['Количество_продаж'])):
    plt.text(i, count + monthly_revenue['Количество_продаж'].max() * 0.01, f'{count:.0f}',
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

orig_city_count = (
    data_set.groupby('ORIG_CITY_CODE')
    .agg(count=('ORIG_CITY_CODE', 'count'),
         revenue=('REVENUE_AMOUNT', 'sum'),
         avg_revenue=('REVENUE_AMOUNT', 'mean'))
    .sort_values('count', ascending=False)
    .head(10)
)

dest_city_count = (
    data_set.groupby('DEST_CITY_CODE')
    .agg(count=('DEST_CITY_CODE', 'count'),
         revenue=('REVENUE_AMOUNT', 'sum'),
         avg_revenue=('REVENUE_AMOUNT', 'mean'))
    .sort_values('count', ascending=False)
    .head(10)
)

plt.figure(figsize=(16, 10))

plt.subplot(2, 2, 1)
plt.bar(orig_city_count.index, orig_city_count["count"], color='lightblue')
plt.title("Топ-10 городов отправления\nпо количеству продаж")
plt.xlabel("Город отправления")
plt.ylabel("Количество продаж")
plt.xticks(rotation=45)
for i, v in enumerate(orig_city_count["count"]):
    plt.text(i, v + orig_city_count["count"].max() * 0.01, f'{v:.0f}', ha='center', va='bottom', fontsize=9)

plt.subplot(2, 2, 2)
plt.bar(dest_city_count.index, dest_city_count["count"], color='lightgreen')
plt.title("Топ-10 городов назначения\nпо количеству продаж")
plt.xlabel("Город назначения")
plt.ylabel("Количество продаж")
plt.xticks(rotation=45)
for i, v in enumerate(dest_city_count["count"]):
    plt.text(i, v + dest_city_count["count"].max() * 0.01, f'{v:.0f}', ha='center', va='bottom', fontsize=9)

plt.subplot(2, 2, 3)
plt.bar(orig_city_count.index, orig_city_count["avg_revenue"], color='orange', alpha=0.7)
plt.title("Средняя стоимость билета по городам отправления")
plt.xlabel("Город отправления")
plt.ylabel("Средняя стоимость билета, руб.")
plt.xticks(rotation=45)

plt.subplot(2, 2, 4)
plt.bar(dest_city_count.index, dest_city_count["avg_revenue"], color='purple', alpha=0.7)
plt.title("Средняя стоимость билета по городам назначения")
plt.xlabel("Город назначения")
plt.ylabel("Средняя стоимость билета, руб.")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

if 'PAX_TYPE' in data_set.columns:
    pax_analysis = data_set.groupby('PAX_TYPE').agg({
        'REVENUE_AMOUNT': ['count', 'sum', 'mean', 'median'],
        'days_before_flight': 'mean'
    }).round(2)

    pax_analysis.columns = ['Количество', 'Сумма_выручки', 'Средняя_выручка', 'Медиана_выручки', 'Ср_дни_до_вылета']
    pax_analysis = pax_analysis.sort_values('Сумма_выручки', ascending=False)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.pie(pax_analysis['Количество'], labels=pax_analysis.index, autopct='%1.1f%%')
    plt.title('Распределение по типам пассажиров')

    plt.subplot(1, 3, 2)
    plt.bar(pax_analysis.index, pax_analysis['Средняя_выручка'])
    plt.title('Средняя стоимость билета по типам пассажиров')
    plt.xticks(rotation=45)
    plt.ylabel('Средняя стоимость билета, руб.')

    plt.subplot(1, 3, 3)
    plt.bar(pax_analysis.index, pax_analysis['Ср_дни_до_вылета'])
    plt.title('Среднее время покупки до вылета')
    plt.xticks(rotation=45)
    plt.ylabel('Дней до вылета')

    plt.tight_layout()
    plt.show()

if 'FFP_FLAG' in data_set.columns:
    data_set['FFP_STATUS'] = data_set['FFP_FLAG'].fillna('Не участник')
    data_set['FFP_STATUS'] = data_set['FFP_STATUS'].replace({'FFP': 'Участник программы'})

    ffp_analysis = data_set.groupby('FFP_STATUS').agg({
        'REVENUE_AMOUNT': ['count', 'sum', 'mean', 'median'],
        'days_before_flight': ['mean', 'median'],
        'PAX_TYPE': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'N/A',
        'ORIG_CITY_CODE': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'N/A'
    }).round(2)

    ffp_analysis.columns = ['Кол-во_продаж', 'Сумма_выручки', 'Ср_стоимость_билета', 'Мед_стоимость_билета',
                            'Ср_дни_до_вылета', 'Мед_дни_до_вылета', 'Частый_тип_пассажира', 'Популярный_город']

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.pie(ffp_analysis['Кол-во_продаж'], labels=ffp_analysis.index, autopct='%1.1f%%', startangle=90)
    plt.title('Распределение по программе лояльности')

    plt.subplot(1, 3, 2)
    bars = plt.bar(ffp_analysis.index, ffp_analysis['Ср_стоимость_билета'], color=['lightblue', 'lightgreen'])
    plt.title('Средняя стоимость билета')
    plt.ylabel('Стоимость билета, руб.')
    plt.xticks(rotation=45)
    for bar, value in zip(bars, ffp_analysis['Ср_стоимость_билета']):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 100,
                 f'{value:.0f} руб.', ha='center', va='bottom', fontsize=10)

    plt.subplot(1, 3, 3)
    bars = plt.bar(ffp_analysis.index, ffp_analysis['Ср_дни_до_вылета'], color=['orange', 'purple'])
    plt.title('Среднее время покупки\nдо вылета')
    plt.ylabel('Дней до вылета')
    plt.xticks(rotation=45)
    for bar, value in zip(bars, ffp_analysis['Ср_дни_до_вылета']):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                 f'{value:.0f} дн.', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()

if 'FOP_TYPE_CODE' in data_set.columns:
    payment_analysis = data_set.groupby('FOP_TYPE_CODE').agg({
        'REVENUE_AMOUNT': ['count', 'sum', 'mean'],
        'days_before_flight': 'mean'
    }).round(2)

    payment_analysis.columns = ['Количество', 'Сумма_выручки', 'Средняя_выручка', 'Ср_дни_до_вылета']
    payment_analysis = payment_analysis.sort_values('Количество', ascending=False).head(10)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.pie(payment_analysis['Количество'], labels=payment_analysis.index, autopct='%1.1f%%')
    plt.title('Распределение способов оплаты')

    plt.subplot(1, 3, 2)
    plt.bar(payment_analysis.index, payment_analysis['Средняя_выручка'])
    plt.title('Средняя стоимость билета\nпо способам оплаты')
    plt.xticks(rotation=45)
    plt.ylabel('Средняя стоимость билета, руб.')

    plt.subplot(1, 3, 3)
    plt.bar(payment_analysis.index, payment_analysis['Количество'])
    plt.title('Количество транзакций\nпо способам оплаты')
    plt.xticks(rotation=45)
    plt.ylabel('Количество транзакций')

    plt.tight_layout()
    plt.show()

daily_sales = data_set.groupby('ISSUE_DATE').agg({
    'ISSUE_DATE': 'count',
    'REVENUE_AMOUNT': 'sum'
}).rename(columns={'ISSUE_DATE': 'ticket_count'}).reset_index()

daily_sales = daily_sales.sort_values('ISSUE_DATE')

daily_sales['ticket_ma_7'] = daily_sales['ticket_count'].rolling(window=7).mean()
daily_sales['ticket_ma_30'] = daily_sales['ticket_count'].rolling(window=30).mean()
daily_sales['revenue_ma_7'] = daily_sales['REVENUE_AMOUNT'].rolling(window=7).mean()

plt.figure(figsize=(16, 12))

plt.subplot(3, 1, 1)
plt.plot(daily_sales['ISSUE_DATE'], daily_sales['ticket_count'], alpha=0.3, label='Факт', linewidth=1, color='blue')
plt.plot(daily_sales['ISSUE_DATE'], daily_sales['ticket_ma_7'], label='Тренд 7 дней', linewidth=2, color='red')
plt.plot(daily_sales['ISSUE_DATE'], daily_sales['ticket_ma_30'], label='Тренд 30 дней', linewidth=2, color='green')
plt.title('ДИНАМИКА ПРОДАЖ БИЛЕТОВ И ТРЕНДЫ', fontsize=14, fontweight='bold')
plt.xlabel('Дата')
plt.ylabel('Количество билетов')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(3, 1, 2)
plt.plot(daily_sales['ISSUE_DATE'], daily_sales['REVENUE_AMOUNT'], alpha=0.3, label='Факт', linewidth=1, color='orange')
plt.plot(daily_sales['ISSUE_DATE'], daily_sales['revenue_ma_7'], label='Тренд выручки (7 дней)', linewidth=2,
         color='red')
plt.title('ДИНАМИКА ВЫРУЧКИ', fontsize=14, fontweight='bold')
plt.xlabel('Дата')
plt.ylabel('Сумма выручки, руб.')
plt.legend()
plt.grid(True, alpha=0.3)

months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']

monthly_pattern = data_set.groupby('issue_month').agg({
    'ISSUE_DATE': 'count',
    'REVENUE_AMOUNT': 'sum'
}).rename(columns={'ISSUE_DATE': 'avg_tickets', 'REVENUE_AMOUNT': 'avg_revenue'})

if 'issue_year' in data_set.columns:
    years_count = data_set['issue_year'].nunique()
    monthly_pattern['avg_tickets'] = monthly_pattern['avg_tickets'] / years_count
    monthly_pattern['avg_revenue'] = monthly_pattern['avg_revenue'] / years_count

plt.subplot(3, 1, 3)
bars = plt.bar(monthly_pattern.index, monthly_pattern['avg_tickets'], alpha=0.7, color='skyblue')
plt.title('ПРОГНОЗ СРЕДНЕМЕСЯЧНЫХ ПРОДАЖ\n(на основе исторических данных)', fontsize=14, fontweight='bold')
plt.xlabel('Месяц')
plt.ylabel('Среднее количество продаж в месяц')
plt.xticks(range(1, 13), months)

for bar, value in zip(bars, monthly_pattern['avg_tickets']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
             f'{value:.0f}', ha='center', va='bottom', fontsize=9)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(monthly_pattern.index, monthly_pattern['avg_tickets'], color='lightblue', alpha=0.7)
plt.title('СЕЗОННЫЙ ПАТТЕРН ПРОДАЖ\n(для прогнозирования)')
plt.xlabel('Месяц')
plt.ylabel('Среднее количество продаж')
plt.xticks(range(1, 13), months, rotation=45)
plt.grid(True, alpha=0.3)

for i, v in enumerate(monthly_pattern['avg_tickets']):
    plt.text(i + 1, v + 10, f'{v:.0f}', ha='center', va='bottom')

plt.subplot(1, 2, 2)
plt.bar(monthly_pattern.index, monthly_pattern['avg_revenue'], color='lightgreen', alpha=0.7)
plt.title('СЕЗОННЫЙ ПАТТЕРН ВЫРУЧКИ\n(для прогнозирования)')
plt.xlabel('Месяц')
plt.ylabel('Средняя выручка, руб.')
plt.xticks(range(1, 13), months, rotation=45)
plt.grid(True, alpha=0.3)

for i, v in enumerate(monthly_pattern['avg_revenue']):
    plt.text(i + 1, v + 10000, f'{v:.0f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()