import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings

warnings.filterwarnings('ignore')


def create_enhanced_sample_data():

    np.random.seed(42)


    brands = ['Galosha', 'Babidas', 'Asic', 'Gunverse', 'Nuke']
    products = {
        'Galosha': ['KA air-9558', 'KA grou-7567', 'KA gre-2749', 'KA earth-3018', 'KA ais-3700'],
        'Babidas': ['BA air-5353', 'BA grou-9248', 'BA gre-3658', 'BA earth-3530', 'BA ais-1740'],
        'Asic': ['AS air-7520', 'AS grou-3318', 'AS gre-2748', 'AS earth-9544', 'AS ais-7331'],
        'Gunverse': ['GU air-3053', 'GU grou-6409', 'GU gre-2865', 'GU earth-4729', 'GU ais-4465'],
        'Nuke': ['NK air-4421', 'NK grou-9880', 'NK gre-7983', 'NK earth-5320', 'NK ais-5028']
    }

    points = ['на Гоголя', 'Центральный', 'Торговый центр', 'Улица Ленина']

    data = []
    start_date = pd.to_datetime('2021-01-01')

    for month in range(24):
        current_date = start_date + pd.DateOffset(months=month)
        for point in points:
            for brand in brands:
                for product in products[brand]:

                    point_factor = np.random.uniform(0.5, 1.5)

                    base_quantity = np.random.randint(15, 80) * point_factor
                    base_price = np.random.randint(5000, 20000)


                    season_factor = 1 + 0.4 * np.sin(2 * np.pi * (month % 12) / 12)


                    trend_factor = 1 + 0.015 * month

                    quantity = max(1, int(base_quantity * season_factor * trend_factor))
                    sales = quantity * base_price
                    cost = sales * np.random.uniform(0.4, 0.7)

                    data.append({
                        'Дата': current_date,
                        'Год': current_date.year,
                        'Год-мес': int(current_date.strftime('%Y%m')),
                        'точка': point,
                        'бренд': brand,
                        'товар': product,
                        'Количество': quantity,
                        'Продажи': sales,
                        'Себестоимость': cost
                    })

    return pd.DataFrame(data)


print("Создание расширенных данных для анализа...")
df = create_enhanced_sample_data()


df['Дата'] = pd.to_datetime(df['Дата'])
df['Месяц'] = df['Дата'].dt.to_period('M')
df['Год'] = df['Дата'].dt.year
df['Квартал'] = df['Дата'].dt.quarter


df['Прибыль'] = df['Продажи'] - df['Себестоимость']
df['Маржинальность'] = (df['Прибыль'] / df['Продажи']) * 100
df['Средняя_цена'] = df['Продажи'] / df['Количество']
df['Продажи_на_точку'] = df['Продажи']  # Для агрегации

print(f"Данные созданы: {len(df)} записей, {df['точка'].nunique()} точек")


print("\n" + "=" * 50)
print("АНАЛИЗ ПО ТОЧКАМ РЕАЛИЗАЦИИ")
print("=" * 50)

point_analysis = df.groupby('точка').agg({
    'Продажи': ['sum', 'mean', 'std'],
    'Количество': 'sum',
    'Прибыль': 'sum',
    'Маржинальность': 'mean',
    'Средняя_цена': 'mean'
}).round(2)

print("Эффективность точек реализации:")
print(point_analysis)


monthly_sales_per_point = df.groupby(['Месяц', 'точка'])['Продажи'].sum().reset_index()
avg_sales_per_point = monthly_sales_per_point.groupby('точка')['Продажи'].mean()

print(f"\nСредние продажи на точку в месяц:")
print(avg_sales_per_point.round(2))

print("\n" + "=" * 50)
print("АНАЛИЗ ПО ТОВАРАМ")
print("=" * 50)

product_analysis = df.groupby('товар').agg({
    'Продажи': ['sum', 'mean', 'std', 'count'],
    'Количество': 'sum',
    'Прибыль': 'sum',
    'Маржинальность': 'mean',
    'Средняя_цена': 'mean'
}).round(2)


df_sorted = df.sort_values(['товар', 'Дата'])
df_sorted['Пред_месяц_продажи'] = df_sorted.groupby('товар')['Продажи'].shift(1)
df_sorted['Рост_продаж_%'] = ((df_sorted['Продажи'] - df_sorted['Пред_месяц_продажи']) /
                              df_sorted['Пред_месяц_продажи']) * 100

product_growth = df_sorted.groupby('товар')['Рост_продаж_%'].mean().round(2)
print("Средний месячный рост по товарам:")
print(product_growth.sort_values(ascending=False).head(10))


fig, axes = plt.subplots(3, 2, figsize=(16, 15))


monthly_total = df.groupby('Месяц').agg({
    'Продажи': 'sum',
    'Количество': 'sum',
    'Прибыль': 'sum'
}).reset_index()
monthly_total['Месяц_str'] = monthly_total['Месяц'].astype(str)

axes[0, 0].plot(monthly_total['Месяц_str'], monthly_total['Продажи'] / 1000,
                marker='o', linewidth=2, label='Продажи')
axes[0, 0].plot(monthly_total['Месяц_str'], monthly_total['Прибыль'] / 1000,
                marker='s', linewidth=2, label='Прибыль')
axes[0, 0].set_title('Динамика товарооборота и прибыли', fontweight='bold')
axes[0, 0].set_ylabel('Тыс. руб')
axes[0, 0].legend()
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(True, alpha=0.3)

point_sales_total = df.groupby('точка')['Продажи'].sum().sort_values(ascending=True)
axes[0, 1].barh(range(len(point_sales_total)), point_sales_total / 1000)
axes[0, 1].set_yticks(range(len(point_sales_total)))
axes[0, 1].set_yticklabels(point_sales_total.index)
axes[0, 1].set_title('Общие продажи по точкам', fontweight='bold')
axes[0, 1].set_xlabel('Продажи, тыс. руб')
axes[0, 1].grid(True, alpha=0.3)


top_margin = product_analysis[('Маржинальность', 'mean')].sort_values(ascending=False).head(10)
axes[1, 0].bar(range(len(top_margin)), top_margin.values)
axes[1, 0].set_xticks(range(len(top_margin)))
axes[1, 0].set_xticklabels([label[:15] + '...' for label in top_margin.index], rotation=45)
axes[1, 0].set_title('Топ-10 товаров по маржинальности', fontweight='bold')
axes[1, 0].set_ylabel('Маржинальность, %')
axes[1, 0].grid(True, alpha=0.3)


for point in df['точка'].unique():
    point_data = monthly_sales_per_point[monthly_sales_per_point['точка'] == point]
    axes[1, 1].plot(point_data['Месяц'].astype(str), point_data['Продажи'] / 1000,
                    marker='o', label=point, linewidth=2)
axes[1, 1].set_title('Динамика продаж по точкам', fontweight='bold')
axes[1, 1].set_ylabel('Продажи, тыс. руб')
axes[1, 1].legend()
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].grid(True, alpha=0.3)

brand_sales = df.groupby('бренд')['Продажи'].sum()
axes[2, 0].pie(brand_sales.values, labels=brand_sales.index, autopct='%1.1f%%',
               colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])
axes[2, 0].set_title('Распределение продаж по брендам', fontweight='bold')


monthly_avg = df.groupby(df['Дата'].dt.month)['Продажи'].mean()
axes[2, 1].bar(monthly_avg.index, monthly_avg.values / 1000, color='skyblue', alpha=0.7)
axes[2, 1].set_title('Сезонность продаж (средние по месяцам)', fontweight='bold')
axes[2, 1].set_xlabel('Месяц')
axes[2, 1].set_ylabel('Средние продажи, тыс. руб')
axes[2, 1].set_xticks(range(1, 13))
axes[2, 1].set_xticklabels(['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн',
                            'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'])
axes[2, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


print("\n" + "=" * 50)
print("ПРОГНОЗИРОВАНИЕ ПРОДАЖ")
print("=" * 50)


def enhanced_forecast(product_data):

    if len(product_data) < 6:
        return None, None, None

    product_data = product_data.sort_values('Месяц')
    product_data['Период'] = range(1, len(product_data) + 1)
    product_data['Месяц_число'] = product_data['Месяц'].dt.month


    X = product_data[['Период']]
    y = product_data['Продажи']

    model = LinearRegression()
    model.fit(X, y)


    next_periods = [len(product_data) + 1, len(product_data) + 2, len(product_data) + 3]
    forecasts = model.predict(np.array(next_periods).reshape(-1, 1))


    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)

    return forecasts[0], mae, forecasts



forecast_results = {}
for product in df['товар'].unique()[:15]:
    product_data = df[df['товар'] == product].groupby('Месяц').agg({
        'Продажи': 'sum',
        'Количество': 'sum'
    }).reset_index()

    forecast, mae, all_forecasts = enhanced_forecast(product_data)
    if forecast is not None:
        forecast_results[product] = {
            'Прогноз_след_месяц': forecast,
            'Точность_MAE': mae,
            'Исторические_средние': product_data['Продажи'].mean(),
            'Рост_%': ((forecast - product_data['Продажи'].mean()) / product_data['Продажи'].mean()) * 100
        }

forecast_df = pd.DataFrame.from_dict(forecast_results, orient='index')
forecast_df = forecast_df.sort_values('Прогноз_след_месяц', ascending=False)

print("Прогноз продаж на следующий месяц (топ-10):")
print(forecast_df.head(10).round(2))


print("\n" + "=" * 60)
print("ФИНАЛЬНЫЙ ОТЧЕТ ПО АНАЛИЗУ ПРОДАЖ")
print("=" * 60)

print(f"\nОБЩИЕ ПОКАЗАТЕЛИ:")
print(f"Период анализа: {df['Дата'].min().strftime('%d.%m.%Y')} - {df['Дата'].max().strftime('%d.%m.%Y')}")
print(f"Общий товарооборот: {df['Продажи'].sum():,.0f} руб")
print(f"Общая прибыль: {df['Прибыль'].sum():,.0f} руб")
print(f"Средняя маржинальность: {df['Маржинальность'].mean():.1f}%")
print(f"Количество чеков: {len(df):,}")
print(f"Товарооборот на точку: {(df['Продажи'].sum() / df['точка'].nunique()):,.0f} руб")

print(f"\nЭФФЕКТИВНОСТЬ ТОЧЕК:")
best_point = point_analysis[('Продажи', 'sum')].idxmax()
print(f"Лучшая точка: {best_point} ({point_analysis.loc[best_point, ('Продажи', 'sum')]:,.0f} руб)")

print(f"\nТОП-5 ТОВАРОВ:")
top_products = product_analysis[('Продажи', 'sum')].sort_values(ascending=False).head(5)
for i, (product, sales) in enumerate(top_products.items(), 1):
    print(f"{i}. {product}: {sales:,.0f} руб")


with pd.ExcelWriter('полный_анализ_продаж_отчет.xlsx') as writer:
    point_analysis.to_excel(writer, sheet_name='Анализ_точек')
    product_analysis.to_excel(writer, sheet_name='Анализ_товаров')
    monthly_total.to_excel(writer, sheet_name='Месячная_динамика')
    forecast_df.to_excel(writer, sheet_name='Прогнозы')
    brand_sales.to_excel(writer, sheet_name='Продажи_по_брендам')

print(f"\nОтчет сохранен в файл: 'полный_анализ_продаж_отчет.xlsx'")
print("\nАнализ завершен! Сформирован полноценный отчет по всем требованиям.")