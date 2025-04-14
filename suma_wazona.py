
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Data.csv")

os.makedirs("img", exist_ok=True)


cechy = {
    'VRAM (GB)': 1,
    'TGP (W)': 0,
    'GPU Score': 1,
    'MSRP ($)': 0,
    'Steam Normalized %': 1
}


wagi = {
    'VRAM (GB)': 0.2,
    'TGP (W)': 0.2,
    'GPU Score': 0.3,
    'MSRP ($)': 0.2,
    'Steam Normalized %': 0.1
}


df_norm = df.copy()
for cecha, stymulant in cechy.items():
    if stymulant:
        df_norm[cecha] = df[cecha] / df[cecha].max()
    else:
        df_norm[cecha] = df[cecha].min() / df[cecha]

df['Wynik sumy ważonej'] = sum(df_norm[col] * wagi[col] for col in cechy.keys())


df['Miejsce (suma ważona)'] = df['Wynik sumy ważonej'].rank(ascending=False).astype(int)

df_sorted = df.sort_values(by='Wynik sumy ważonej', ascending=False)
top10 = df_sorted.head(10)

plt.figure(figsize=(12, 6))
plt.barh(top10['Model Name'][::-1], top10['Wynik sumy ważonej'][::-1], color='cornflowerblue', edgecolor='black')
plt.xlabel("Wynik sumy ważonej")
plt.title("TOP 10 kart graficznych – suma ważona")
plt.tight_layout()
plt.savefig("img/suma_top10_bar.png")
plt.close()
