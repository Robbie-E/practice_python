# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:42:30 2021

@author: Robertson
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('BankChurners.csv')

# Map categorical features to a numerical value
del df['CLIENTNUM']
del df['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1']
del df['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2']

def find_cats(column):
    """
    find the categories for a categorical variable
    column is of format df.column_name
    """
    return pd.Categorical(column).categories

def find_cats_freq(data, column):
    """
    finds category and their frequencies
    data is the data frame
    column is a string
    """
    return data.groupby(column)[column].count()
    
def map_to_num(column, cats, vals):
    """
    maps the categories to a number
    column is of format df.column_name
    """
    map_dict = {cats[i]:vals[i] for i in range(len(cats))}
    return column.map(map_dict)

flag_cats = find_cats(df.Attrition_Flag)
flag_vals = [1,0]
df.Attrition_Flag = map_to_num(df.Attrition_Flag, flag_cats, flag_vals)

gender_cats = find_cats(df.Gender)
gender_vals = [0,1]
df.Gender = map_to_num(df.Gender, gender_cats, gender_vals)

educ_cats = find_cats(df.Education_Level)
educ_vals = [i for i in range(len(find_cats(df.Education_Level)))]
df.Education_Level = map_to_num(df.Education_Level, educ_cats, educ_vals)

mar_cats = find_cats(df.Marital_Status)
mar_vals = [i for i in range(len(find_cats(df.Marital_Status)))]
df.Marital_Status = map_to_num(df.Marital_Status, mar_cats, mar_vals)

card_cats = find_cats(df.Card_Category)
card_vals = [i for i in range(len(find_cats(df.Card_Category)))]
df.Card_Category = map_to_num(df.Card_Category, card_cats, card_vals)

def extract_nums(string):
    """
    extract numbers from string categories
    """
    num_list = []
    mods1 = string.replace('$', '')
    mods2 = mods1.replace('K', '')
    for s in mods2.split(' '):
        try:
            num_list.append(int(s))
        except Exception:
            pass
    return np.mean(num_list)

def map_range_cats(column):
    """
    map the Income_Category feature to the midpoint of each interval
    """
    cats = find_cats(column)
    range_means = []
    for s in cats:
        if s == 'Unknown':
            range_means.append(0)
        else:
            range_means.append(extract_nums(s))
    sorted_range_means = np.sort(range_means)
    order_idx = np.argsort(range_means)
    cats = cats[order_idx]
    # Replace the Unknown income with the average of the midpoints
    # This could be done with a weighted average (using the frequency counts of other intervals)
    sorted_range_means[0] = np.mean(sorted_range_means[1:])
    new_order_idx = np.argsort(sorted_range_means)
    #income is in units of $10K
    return np.sort(sorted_range_means)/10, cats[new_order_idx]

income_mids, income_cats = map_range_cats(df.Income_Category)
df.Income_Category = map_to_num(df.Income_Category, income_cats, income_mids) 

# Visualize some variables
def cat_count(data, column_str, criteria):
    """
    access the normalized counts of each category
    """
    ct1 = []
    ct2 = []
    for i in range(len(find_cats_freq(data, column_str))):
        ct1.append(find_cats_freq(data[criteria], column_str)[i])
        ct2.append(find_cats_freq(data, column_str)[i])
    return np.array(ct1)/np.array(ct2)

criteria = df.Attrition_Flag == 1

#plt.bar(find_cats(df.Card_Category), cat_count(df, 'Card_Category', criteria))
#plt.xlabel('Card Holder categories (B/G/S/P)')
#plt.ylabel('Fraction Attrited (per Card Holder Category)')

#plt.bar(find_cats(df.Months_Inactive_12_mon), cat_count(df, 'Months_Inactive_12_mon', criteria))
#plt.xlabel('Months Inactive in last 12 months')
#plt.ylabel('Fraction Attrited (per count in a category)')

#plt.hist(df.Avg_Utilization_Ratio[df.Attrition_Flag == 1], bins=20)
#plt.xlabel('Average Card Utilization Ratio')
#plt.ylabel('log Count Attrited')
#plt.yscale('log')

plt.hist(df.Months_on_book[df.Attrition_Flag == 1], bins=20)
plt.xlabel('Months on book')
plt.ylabel('Count Attrited')