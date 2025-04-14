import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt


os.makedirs("img", exist_ok=True)


df = pd.read_csv("Data.csv")

cechy = ['VRAM (GB)', 'TGP (W)', 'GPU Score', 'MSRP ($)', 'Steam Normalized %']
correlation = df[cechy].corr()


plt.figure(figsize=(10, 8))  
sns.set(font_scale=1.1)      
sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True,
            cbar_kws={"shrink": 0.8}, linewidths=0.5, linecolor='gray')

plt.title('Macierz korelacji cech kart graficznych')
plt.tight_layout()  
plt.savefig("img/heatmapv2.png")
plt.close()