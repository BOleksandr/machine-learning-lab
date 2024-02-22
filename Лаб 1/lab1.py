import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Відкрити та зчитати файл з даними. 
df = pd.read_csv('Vehicle_Sales.csv')

# 2. Визначити та вивести кількість записів та кількість полів у кожному 
# записі.
print('2.')
print(f'Rows: {len(df)} columns: {len(df.columns)}')

# 3. Вивести 26 перших та 5К-3 останніх записів.
print('3.')
print(df.head(26))
print()
print(df.tail(92))

# 4. Визначити та вивести тип полів кожного запису.
print('4.')
print(df.dtypes)

# 5. Привести поля, що відповідають обсягам продаж, до числового вигляду
# (показати, що це виконано).
columns_sales = ['Total Sales New', 'Total Sales Used']
for i in columns_sales:
    df[i] = df[i].apply(lambda x: x.replace('$', '')).astype(np.int64)

print('5.')
print(df.dtypes)


# 6. Ввести нові поля: 
# a. Сумарний обсяг продаж автомобілів (нових та б/в) у кожний період; 
df['Total Car'] = df['New'] + df['Used']

# b. Сумарний дохід від продажу автомобілів (нових та б/в) у кожний
# період; 
df['Total Sales'] = df[columns_sales[0]] + df[columns_sales[1]]
# c. Різницю в обсязі продаж нових та б/в автомобілів у кожній період. 
df['Difference New And Used'] = df['New'] - df['Used']

# pd.set_option('display.max_columns', None)
# print(df)
print('6.')
print(df.dtypes)

# 7. Змінити порядок розташування полів таким чином: Рік, Місяць, 
# Сумарний дохід, Дохід від продажу нових автомобілів, Дохід від
# продажу б/в автомобілів, Сумарний обсяг продаж, Обсяг продаж нових
# автомобілів, Обсяг продаж б/в автомобілів, Різниця між обсягами
# продаж нових та б/в автомобілів.
df = df[['Year', 'Month', 'Total Sales', 'Total Sales New', 'Total Sales Used', 'Total Car', 'New', 'Used', 'Difference New And Used']]
print('7.')
print(df.columns)

# 8. Визначити та вивести: 
date = ['Year', 'Month']
# a. Рік та місяць, у які нових автомобілів було продано менше за б/в; 
new_less_used = df[df['Difference New And Used'] < 0][date]
print('8.a')
print(new_less_used)

# b. Рік та місяць, коли сумарний дохід був мінімальним; 
min_total_sales = df[df['Total Sales'] == df['Total Sales'].min()][date]
print('8.b')
print(min_total_sales)

# c. Рік та місяць, коли було продано найбільше б/в авто.
max_used = df[df['Used'] == df['Used'].max()][date]
print('8.c')
print(max_used)

# 9. Визначити та вивести: 
# a. Сумарний обсяг продажу транспортних засобів за кожен рік; 
sum_car_year = df.groupby('Year')['Total Car'].sum()
print('9.a')
print(sum_car_year)

# b. Середній дохід від продажу б/в транспортних засобів в місяці 02 (Feb), 
average_income_used_feb = df[df['Month'] == 'FEB']['Total Sales Used'].mean()
print('9.b')
print('FEB:', average_income_used_feb)

# 10. Побудувати стовпчикову діаграму обсягу продаж нових авто у 2015 році
 
sale_new_in_2015 = df[df['Year'] == 2015]

plt.bar(sale_new_in_2015['Month'], sale_new_in_2015['New'])
plt.xlabel('Місяць')
plt.ylabel('Кількість авто')
plt.title('Обсяг продаж нових авто у 2015 році')
plt.show()

# 11. Побудувати кругову діаграму сумарного обсягу продаж за кожен рік.
sales_volume_for_each_year = df.groupby('Year')['Total Car'].sum()
plt.pie(sales_volume_for_each_year, labels=sales_volume_for_each_year.index, autopct='%1.1f%%')
plt.title('Сумарний обсяг продаж за кожен рік')
plt.show()

# 12. Побудувати на одному графіку: 
# a. Сумарний дохід від продажу нових авто; 
# b. Сумарний дохід від продажу старих авто.
total_income_sale_new_cars = df.groupby('Year')['Total Sales New'].sum()
total_income_sale_used_cars = df.groupby('Year')['Total Sales Used'].sum()

plt.plot(total_income_sale_new_cars.index, total_income_sale_new_cars, label = 'Дохід від продажу нових авто')
plt.plot(total_income_sale_used_cars.index, total_income_sale_used_cars, label = 'Дохід від продажу старих авто')
plt.xlabel('Рік')
plt.ylabel('Сумарний дохід')
plt.legend()
plt.title('Сумарний дохід від продажу нових та старих авто за кожен рік')
plt.show()