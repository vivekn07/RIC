# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:49:23 2019

@author: MyHome
"""

from scipy import stats
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("C:/Users/VivekN7/Desktop/MU Practical/RIC Practical/3. T-Test/Support Files/blood_pressure.csv")

print(df[['bp_before','bp_after']].describe())

#First let’s check for any significant outliers in 
#each of the variables.
#df[['bp_before', 'bp_after']].plot(kind='box')
# This saves the plot as a png file
#plt.savefig('boxplot_outliers.png')

# make a histogram to differences between the two scores.
#df['bp_difference'] = df['bp_before'] - df['bp_after']

#df['bp_difference'].plot(kind='hist', title= 'Blood Pressure Difference Histogram')
#Again, this saves the plot as a png file
#plt.savefig('blood pressure difference histogram.png')
#stats.probplot(df['bp_difference'], plot= plt)
#plt.title('Blood pressure Difference Q-Q Plot')
#plt.savefig('blood pressure difference qq plot.png')
#print(stats.shapiro(df['bp_difference']))
ttest,pval = stats.ttest_rel(df['bp_before'], df['bp_after'])
print(pval)
print(stats.ttest_rel(df['bp_before'], df['bp_after']))
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")

