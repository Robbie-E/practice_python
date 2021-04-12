# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:42:30 2021

@author: Robertson
"""

import pandas as pd
import numpy as np

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

# Normalize numerical features
def normalize(column):
    """
    normalizes a column
    column is in df.column_name format
    """
    return (column - np.mean(column))/np.std(column)   

df.Customer_Age = normalize(df.Customer_Age)
df.Dependent_count = normalize(df.Dependent_count)
df.Income_Category = normalize(df.Income_Category)
df.Months_on_book = normalize(df.Months_on_book)
df.Total_Relationship_Count = normalize(df.Total_Relationship_Count)
df.Months_Inactive_12_mon = normalize(df.Months_Inactive_12_mon)
df.Contacts_Count_12_mon = normalize(df.Contacts_Count_12_mon)
df.Credit_Limit = normalize(df.Credit_Limit)
df.Total_Revolving_Bal = normalize(df.Total_Revolving_Bal)
df.Avg_Open_To_Buy = normalize(df.Avg_Open_To_Buy)
df.Total_Amt_Chng_Q4_Q1 = normalize(df.Total_Amt_Chng_Q4_Q1)
df.Total_Trans_Amt = normalize(df.Total_Trans_Amt)
df.Total_Trans_Ct = normalize(df.Total_Trans_Ct)
df.Total_Ct_Chng_Q4_Q1 = normalize(df.Total_Ct_Chng_Q4_Q1)
#df.Avg_Utilization_Ratio = normalize(df.Avg_Utilization_Ratio)

df.to_csv(".\data.csv", index=False)  