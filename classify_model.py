import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

###Analyze Data####
data = pd.read_csv('descriptors2.csv')
#print(data.describe())
#print(data.head())
print("Size", data.shape)

corr = data.corr().abs()
corr2 = corr.unstack()
#print(corr2.sort_values(kind="quicksort", ascending=False))
#print("Corr\n", corr2.value_counts())
#corr2.value_counts().plot(kind='barh')

#print((data.max()-data.min()).sort_values(kind="quicksort", ascending=False))
#print("Range\n", (data.max()-data.min()).value_counts())
#(data.max()-data.min()).value_counts().plot(kind='barh')

#print(data.isnull().sum().sort_values(kind="quicksort", ascending=False))
#print("Null\n", data.isnull().sum().value_counts().sort_values(kind="quicksort"))
#data.isnull().sum().value_counts().plot(kind='barh')

###Data Cleaning#####
#remove columns that have 0 range (183 of them)
#print out columns with inf range (print sample values)
#test out first dropping all columns with null values
#try iterative imputer

from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

"""
data = data.replace([np.inf, -np.inf], np.nan)
data.dropna(inplace=True)
"""
        

for col in data.columns:
    if np.inf in set(data[col]):
        data = data.drop(columns=[col])
    elif -np.inf in set(data[col]):
        data = data.drop(columns=[col])
    elif np.nan in set(data[col]):
        data = data.drop(columns=[col])


print(np.any(np.isnan(data)))
print(np.all(np.isfinite(data)))
print(data.shape)

"""
imp_mean = IterativeImputer(random_state=0)
imp_mean.fit(data.to_numpy())
IterativeImputer(random_state=0)
data2 = imp_mean.transform(data.to_numpy())
print(data2.isnull().sum().sort_values(kind="quicksort", ascending=False))
print("Range\n", (data2.max()-data2.min()).value_counts())
"""
