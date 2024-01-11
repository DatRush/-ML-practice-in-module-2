import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv("train.csv", encoding = 'ISO-8859-1', low_memory = False)

skaler = StandardScaler()

df_matrix = df['balance_due'].values.reshape(-1, 1)
std_scaled = skaler.fit_transform(df_matrix)

min_value = np.min(std_scaled)
print(round(min_value, 5))