# -*- coding: utf-8 -*-
"""5A One Sample Z-test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u3CUH_ZqBq5j1CKCEsQpiPasqvlPXWov
"""

from statsmodels.stats import weightstats as stests
import pandas as pd
from scipy import stats

# Uploading and the Importing "blood pressure.csv" file
df = pd.read_csv("C:/Users/VivekN7/Desktop/MU Practical/RIC Practical/5 - Z-Test/Support Files/blood_pressure.csv")

df[['bp_before','bp_after']].describe()

print(df)

ztest, pval = stests.ztest(df['bp_before'], x2 = None, value = 156)

print(float(pval))

if pval < 0.05:
  print("Reject Null Hypothesis")
else:
  print("Accept Null Hpothesis")
