import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("img", exist_ok=True)


df = pd.read_csv("Data.csv")


df['Performance per $'] = df['GPU Score'] / df['MSRP ($)']
df['Performance per W'] = df['GPU Score'] / df['TGP (W)']


summary = df.groupby("Manufacturer")[["MSRP ($)", "Performance per $", "Performance per W", "Steam Normalized %"]].mean().round(2)

fig, axs = plt.subplots(2, 2, figsize=(14, 10))


axs[0, 0].bar(summary.index, summary["MSRP ($)"], color='skyblue', edgecolor='black')
axs[0, 0].set_title("Średnia cena MSRP ($)")
axs[0, 0].set_ylabel("USD")

axs[0, 1].bar(summary.index, summary["Performance per $"], color='lightgreen', edgecolor='black')
axs[0, 1].set_title("Średnia wydajność za 1$")


axs[1, 0].bar(summary.index, summary["Performance per W"], color='salmon', edgecolor='black')
axs[1, 0].set_title("Średnia wydajność na 1W")


axs[1, 1].bar(summary.index, summary["Steam Normalized %"], color='orange', edgecolor='black')
axs[1, 1].set_title("Średni udział rynkowy (Steam Normalized %)")

plt.suptitle("Analiza producentów – średnie parametry", fontsize=16)
plt.tight_layout()
plt.savefig("img/analiza_producentow.png")
plt.close()
