import pandas as pd
import numpy as np

# Генерация данных для tr_mcc_codes
mcc_codes = {
    'mcc_code': ['1234', '5678', '9101', '1121', '3141'],
    'description': ['Groceries', 'Restaurants', 'Gas', 'Utilities', 'Entertainment']
}
tr_mcc_codes = pd.DataFrame(mcc_codes)
tr_mcc_codes.to_csv('data/tr_mcc_codes.csv', index=False)

# Генерация данных для tr_types
tr_types = {
    'tr_type': ['purchase', 'refund', 'transfer'],
    'description': ['Purchase Transaction', 'Refund Transaction', 'Transfer Transaction']
}
tr_types_df = pd.DataFrame(tr_types)
tr_types_df.to_csv('data/tr_types.csv', index=False)

# Генерация данных для transactions
num_transactions = 1500000
transactions = {
    'transaction_id': range(num_transactions),
    'mcc_code': np.random.choice(tr_mcc_codes['mcc_code'], size=num_transactions),
    'tr_type': np.random.choice(tr_types_df['tr_type'], size=num_transactions),
    'amount': np.random.uniform(-1000, 1000, size=num_transactions),
}
transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv('data/transactions.csv', index=False)

# Генерация данных для customers_gender_train
customers_gender = {
    'customer_id': range(1, 1001),
    'gender': np.random.choice(['M', 'F'], size=1000)
}
customers_gender_train = pd.DataFrame(customers_gender)
customers_gender_train.to_csv('data/customers_gender_train.csv', index=False)
