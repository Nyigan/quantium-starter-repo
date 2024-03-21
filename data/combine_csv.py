import pandas as pd

df1 = pd.read_csv('daily_sales_data_0.csv')
df2 = pd.read_csv('daily_sales_data_1.csv')
df3 = pd.read_csv('daily_sales_data_2.csv')

combined_df = pd.concat([df1, df2, df3], ignore_index=True)

new_df = combined_df[combined_df['product'] == 'pink morsel']

new_df['sales']=new_df['price'] * new_df['quantity']

new_col_created = ['sales','date', 'region']

new_df[new_col_created].to_csv('combined_sales_data.csv', index=False)


