import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv("modul_2/train.csv", encoding = 'ISO-8859-1', low_memory = False)

sqrt_data = np.sqrt(df.balance_due[df.balance_due > 0])

mean_value = np.mean(sqrt_data)
median_value = np.median(sqrt_data)

x = (mean_value - median_value)
result = np.abs(x)

print(round(result, 6))