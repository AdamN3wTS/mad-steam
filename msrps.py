import seaborn as sns
import pandas as  pd
import os
import matplotlib.pyplot as plt
os.makedirs("img",exist_ok=True)
df= pd.read_csv("Data.csv")

#msrp

sns.boxplot(x="Manufacturer",y="MSRP ($)",data=df)
plt.title("Cena MSRP wg producenta")
plt.savefig("img/msrp.png")
plt.close()
