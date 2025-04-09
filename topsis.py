import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


os.makedirs("img", exist_ok=True)


df = pd.read_csv("Data.csv")


features = {
    'VRAM (GB)': 1,
    'TGP (W)': 0,
    'GPU Score': 1,
    'MSRP ($)': 0,
    'Steam Normalized %': 1
}


X = df[list(features.keys())].values


X_norm = X / np.sqrt((X**2).sum(axis=0))

features_array = np.array(list(features.values()))
ideal_plus = np.max(X_norm, axis=0) * features_array + np.min(X_norm, axis=0) * (1 - features_array)
ideal_minus = np.min(X_norm, axis=0) * features_array + np.max(X_norm, axis=0) * (1 - features_array)


d_plus = np.sqrt(((X_norm - ideal_plus)**2).sum(axis=1))
d_minus = np.sqrt(((X_norm - ideal_minus)**2).sum(axis=1))


df['TOPSIS Score'] = d_minus / (d_plus + d_minus)
df['TOPSIS Rank'] = df['TOPSIS Score'].rank(ascending=False).astype(int)


df_sorted = df.sort_values(by='TOPSIS Score', ascending=False)
top10 = df_sorted.head(10)

plt.figure(figsize=(12, 6))
plt.barh(top10['Model Name'][::-1], top10['TOPSIS Score'][::-1], color='steelblue', edgecolor='black')
plt.xlabel("TOPSIS Score")
plt.title("TOP 10 kart graficznych wg TOPSIS")
plt.tight_layout()
plt.savefig("img/topsis_top10_bar.png")
plt.close()


producer_counts = top10['Manufacturer'].value_counts()
colors = ['gold', 'skyblue', 'lightcoral']  
plt.figure(figsize=(6, 6))
plt.pie(producer_counts, labels=producer_counts.index, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Udział producentów w TOP 10 wg TOPSIS")
plt.savefig("img/topsis_top10_pie.png")
plt.close()
