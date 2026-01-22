import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DIAMONDS_DATASET = "https://raw.githubusercontent.com/aiedu-courses/stepik_eda_and_dev_tools/main/datasets/diamonds_good.csv"

df = pd.read_csv(DIAMONDS_DATASET)

y_meadin = df[f"'y'"].median()
df[f"'y'"] = df[f"'y'"].fillna(y_meadin)

max(df[df.cut == "Fair"]["carat"])

round(len(df[(df.table >= 55) & (df.table <= 60) & (df.depth > 59) & (df.depth < 62.5)]) / len(df), 2)

print(df[(df.table >= 55) & (df.table <= 60) & (df.depth > 59) & (df.depth < 62.5)]["price"].median())
print(df.price.median())

len(df.groupby('clarity'))

len(df[(df.clarity == "VVS1") + (df.clarity == "VVS2")])

plt.figure(figsize=(6,4))
#Задание 7
sns.barplot(x='clarity', y='price', data = df, palette='summer')
plt.title('clarity - price')
plt.show();
#Задание 8
df.groupby(['cut','clarity']).agg(PriceMean=('price','mean'),
                      PriceMedian=('price', 'median')).sort_values(by='PriceMean', ascending=False)

len(df[(df.y == 0) + (df.x == 0) + (df.z == 0)])

x_mean = df.x.mean()
y_mean = df.y.mean()
round(len(df[(df.x > x_mean) & (df.y > y_mean)]) / len(df) * 100)
#Задание 2.7
round(len(df[(df.carat >= 1) & (df.z < df.z.median())]) / len(df[df.carat >= 1]),4)
#Задание 2.8
df.groupby('color', as_index=False).agg(
        медианная_стоимость=('price', 'median'),
        медианный_вес=('carat', 'median')
    ).sort_values(by='медианная_стоимость', ascending=False)
