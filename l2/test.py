import pandas as pd

df = pd.read_csv('data.csv')

filtered_data = df[df['Quantity'] > 20]['Item_Total']

info = filtered_data.mean()
print(info)
