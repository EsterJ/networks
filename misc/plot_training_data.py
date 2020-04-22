import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('outputs/training_data.csv')
df = df.drop(df.columns[0], 1)
df = df.interpolate(limit_area='inside')
df.plot(x=df.columns[0])
plt.show()
