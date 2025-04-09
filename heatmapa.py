import pandas as  pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
os.makedirs("img",exist_ok=True)
df= pd.read_csv("Data.csv")
correlation = df[['VRAM (GB)', 'TGP (W)', 'GPU Score', 'MSRP ($)', 'Steam Normalized %']].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Macierz korelacji cech kart graficznych')
plt.savefig("img/heatmap.png")
plt.close()
