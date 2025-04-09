import pandas as  pd
import os
import matplotlib.pyplot as plt
os.makedirs("img",exist_ok=True)
df= pd.read_csv("Data.csv")
steam_share = df.groupby('Manufacturer')['Steam Normalized %'].sum()

steam_share.plot(kind='bar')
plt.ylabel('Suma Steam Normalized %')
plt.title('Udział rynkowy producentów (Steam Normalized %)')
plt.savefig("img/ryneksteam.png")
plt.close()