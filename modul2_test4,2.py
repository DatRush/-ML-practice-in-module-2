import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("modul_2/train.csv", encoding='ISO-8859-1', low_memory=False)

dt_issued_date = pd.to_datetime(df.ticket_issued_date.dropna())
df['is_weekend'] = dt_issued_date.dt.weekday > 4
filtered_df = df[df['is_weekend'] == True]

print(len(filtered_df))