import pandas as pd
import numpy as np

df = pd.read_csv("Data.csv")

features = {
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

X = df[list(features.keys())].values
X_norm = X / np.sqrt((X**2).sum(axis=0))

features_array = np.array(list(features.values()))
ideal_plus = np.max(X_norm, axis=0) * features_array + np.min(X_norm, axis=0) * (1 - features_array)
ideal_minus = np.min(X_norm, axis=0) * features_array + np.max(X_norm, axis=0) * (1 - features_array)

d_plus = np.sqrt(((X_norm - ideal_plus)**2).sum(axis=1))
d_minus = np.sqrt(((X_norm - ideal_minus)**2).sum(axis=1))

df['TOPSIS'] = d_minus / (d_plus + d_minus)

df_norm = df.copy()
for cecha, stymulant in features.items():
    if stymulant:
        df_norm[cecha] = df[cecha] / df[cecha].max()
    else:
        df_norm[cecha] = df[cecha].min() / df[cecha]

df['Suma ważona'] = sum(df_norm[col] * wagi[col] for col in features.keys())

df['Iloczyn ważony'] = np.prod(
    [df_norm[col] ** wagi[col] for col in features.keys()],
    axis=0
)

df['TOPSIS Rank'] = df['TOPSIS'].rank(ascending=False).astype(int)
df['Miejsce (suma ważona)'] = df['Suma ważona'].rank(ascending=False).astype(int)
df['Miejsce (iloczyn ważony)'] = df['Iloczyn ważony'].rank(ascending=False).astype(int)

df.to_csv("Data_with_scores_and_ranks.csv", index=False)
