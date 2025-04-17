import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data_with_scores_and_ranks.csv")

df_scores = df[['Model Name', 'TOPSIS', 'Suma ważona', 'Iloczyn ważony']]

correlation_full = df_scores.drop(columns='Model Name').corr(method='spearman')

correlation_full.to_csv("korelacja_wynikow_full.csv")

plt.figure(figsize=(6, 5))
sns.heatmap(correlation_full, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Korelacja wyników – wszystkie modele (Spearman)")
plt.tight_layout()
plt.savefig("img/korelacja_wynikow_full.png")
plt.close()
