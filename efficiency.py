import pandas as  pd
import os
import matplotlib.pyplot as plt
os.makedirs("img",exist_ok=True)
df= pd.read_csv("Data.csv")

df['Performance per $'] = df['GPU Score'] / df['MSRP ($)']
df['Performance per W'] = df['GPU Score'] / df['TGP (W)']
summary = df.groupby("Manufacturer")[["MSRP ($)", "Performance per $", "Performance per W"]].mean().round(2)
fig, axs = plt.subplots(1, 3, figsize=(18, 5))


axs[0].bar(summary.index, summary["MSRP ($)"], color='skyblue', edgecolor='black')
axs[0].set_title("Średnia cena MSRP ($)")
axs[0].set_ylabel("USD")

axs[1].bar(summary.index, summary["Performance per $"], color='lightgreen', edgecolor='black')
axs[1].set_title("Wydajność za $")

axs[2].bar(summary.index, summary["Performance per W"], color='salmon', edgecolor='black')
axs[2].set_title("Wydajność na 1W")

plt.suptitle("Średnie parametry wg producenta", fontsize=16)
plt.tight_layout()
plt.savefig("img/producent_porownanie.png")
plt.close()

