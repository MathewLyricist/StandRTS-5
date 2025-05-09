# Загрузка необходимых библиотек
import pandas as pd
import matplotlib.pyplot as plt

# 1. Загрузка данных
tr_mcc_codes = pd.read_csv('data/tr_mcc_codes.csv')
tr_types = pd.read_csv('data/tr_types.csv')
transactions = pd.read_csv('data/transactions.csv', nrows=1000000)
customers_gender_train = pd.read_csv('data/customers_gender_train.csv')

# 2. Объединение таблиц
transactions = transactions.merge(tr_mcc_codes, on='mcc_code', how='inner')
transactions = transactions.merge(tr_types, on='tr_type', how='inner')
transactions = transactions.merge(customers_gender_train, left_on='transaction_id', right_on='customer_id', how='left')

# 3. Создание нового столбца mcc_code+tr_type
transactions['mcc_code+tr_type'] = transactions['mcc_code'].astype(str) + '+' + transactions['tr_type'].astype(str)

# 4. Фильтрация положительных значений amount
transactions = transactions[transactions['amount'] > 0]

# 5. Рассчет средних значений по категориям mcc_code+tr_type, где 5 <= количество наблюдений <= 30
mean_values = transactions.groupby('mcc_code+tr_type').agg(count=('amount', 'size'), mean_amount=('amount', 'mean'))
result = mean_values[(mean_values['count'] >= 5) & (mean_values['count'] <= 30)]

# Округление до двух знаков после запятой
mean_result = result['mean_amount'].mean()
mean_result_rounded = round(mean_result, 2)

print('Среднее значение:', mean_result_rounded)

plt.figure(figsize=(10, 7))
plt.pie(result['mean_amount'], labels=result.index, autopct='%1.1f%%')
plt.title('Распределение средних значений по категориям mcc_code+tr_type')
plt.axis('equal')  # Для того, чтобы круг смотрелся правильно
plt.show()