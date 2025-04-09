import pandas as pd
import os
os.makedirs("img",exist_ok=True)
df = pd.read_csv("Data.csv")
#Histogramy rozkładu
import matplotlib.pyplot as plt

fig,axs = plt.subplots(2,2,figsize=(12,8))

axs[0,0].hist(df['VRAM (GB)'],bins=10,edgecolor='black',linewidth=0.5)
axs[0, 0].set_title('Rozkład VRAM (GB)')

axs[0, 1].hist(df['TGP (W)'], bins=10,edgecolor='black',linewidth=0.5)
axs[0, 1].set_title('Rozkład TGP (W)')

axs[1, 0].hist(df['GPU Score'], bins=10,edgecolor='black',linewidth=0.5)
axs[1, 0].set_title('Rozkład GPU Score')

axs[1, 1].hist(df['MSRP ($)'], bins=10,edgecolor='black',linewidth=0.5)
axs[1, 1].set_title('Rozkład MSRP ($)')

plt.tight_layout()
plt.savefig("img/histogramy_cech.png")
plt.close()
