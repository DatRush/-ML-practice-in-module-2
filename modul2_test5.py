import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("modul_2/train.csv", encoding='ISO-8859-1', low_memory=False)

def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))[0]

o = outliers_iqr(df.balance_due.dropna())

outlier_labels = df.index[o]

df_cleaned = df.drop(outlier_labels)

min_value = df_cleaned['balance_due'].min()
max_value = df_cleaned['balance_due'].max()

print(max_value - min_value)