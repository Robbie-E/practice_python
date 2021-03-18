# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:13:29 2021

@author: Robertson
"""
"""
Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

0) remove negative integers
1) remove duplicates from list
2) sort the list
3) check if 
"""

def solution1(A):
    sorted_nodup_A = list(dict.fromkeys(A.sort()))
    sorted_nodup_A = sorted_nodup_A[sorted_nodup_A > 0]
    if max(sorted_nodup_A) < 0:
        return 1
    else:
        for i in range(len(sorted_nodup_A)-1):
            if sorted_nodup_A[i+1]!=sorted_nodup_A[i]+1:
                return sorted_nodup_A[i+1]
            else: 
                return sorted_nodup_A[-1]+1

"""
O(n) or O(nlogn) time complexity 
"""        
def solution(A):
    A = [a for a in A if a>0]
    #if all neg vals or min is > 1
    if len(A) == 0 or min(A) > 1:
        abs_int = 1
    else: #A is modified to remove negative integers and sort
        A.sort()
        abs_int = A[-1]+1 
        #if all int are present in order, then max(A)+1 is absent
        for i in range(len(A)-1):
            if A[i+1] == A[i] or A[i+1] == A[i]+1:
                continue
            else:
                abs_int = A[i]+1
                break #we consider (smallest absent) first instance
    return abs_int


