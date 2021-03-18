# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:44:54 2021

@author: Robertson
"""
"""
Given an array a that contains only numbers in the range from 1 to len(a), 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, 
return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. 
If there are no such elements, return -1.
"""
#import numpy as np
#def firstDuplicate(a):
#    indices = np.argsort(np.array(a))
#    dup_index = []
#    for ind_index in range(len(indices)-1):
#        if a[indices[ind_index]] == a[indices[ind_index+1]]:
#            dup_index.append(indices[ind_index+1])
#    if len(dup_index) == 0:
#        return -1
#    else:
#        return a[np.sort(dup_index)[0]]
    
import numpy as np
def firstDuplicate1(a):
    indices = np.argsort(np.array(a))
    first_dup_index = []
    for ind_index in range(len(indices)-1):
        if a[indices[ind_index]] == a[indices[ind_index+1]]:
            first_dup_index.append(indices[ind_index+1])
        else:
            continue
    if len(first_dup_index) == 0:
        return -1
    else:
        return a[np.sort(first_dup_index)[0]]
        
def firstDuplicate2(a):
    unique_elements = []
    for element in a:
        if element not in unique_elements:
            unique_elements.append(element)
        else:
            break
    if len(unique_elements) == len(a):
        return -1
    else:
        return element
"""
long execution time
"""    
def firstDuplicate3(a):
    unique_elements = []
    for element in a:
        if element in unique_elements:
            return element
        unique_elements.append(element)
    return -1

"""
better execution time
"""
def firstDuplicate4(a):
    #set remove duplicates from array, unordered
    #scan along the array and collect unique elements
    unique_elements = set()
    for element in a:
        if element in unique_elements:
            return element
        unique_elements.add(element)
    return -1
