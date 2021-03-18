# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:03:30 2021

@author: Robertson
"""

"""
An array A consisting of N integers is given. An equilibrium index of this array is any integer P such that 0 ≤ P < N and the sum of elements of lower indices is equal to the sum of elements of higher indices, i.e.
A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or if P = N−1.
There can be more than 1 equilibrium index.
"""

def solution(A):
    total = sum(A)
    left = 0
    eq_indices = []
    for index in range(len(A)):
        if left == total - (A[index]+left):
            eq_indices.append(index)
        left += A[index]
    if len(eq_indices) == 0:
        return -1
    else:
        return eq_indices
    