import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("modul_2/train.csv", encoding='ISO-8859-1', low_memory=False)
df_selected = df[['balance_due', 'payment_amount']]

pf = PolynomialFeatures(3)
poly_features = pf.fit_transform(df_selected)

mean_values = np.mean(poly_features, axis=0)
max_mean_index = mean_values.argmax()

print(max_mean_index)
