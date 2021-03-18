# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:01:10 2021

@author: Robertson

Write a function:
def solution(A) such that given the binary representation of a positive integer, determine the 
largest sequence of 0's in between 1's
"""

def bit(N):
    return "{0:b}".format(N)

#bin_rep is a string
def gap(bin_rep):
    bin_gaps = []
    for start_index in range(len(bin_rep)-1):
        if bin_rep[start_index] == '1':
            bit_index = start_index + 1
            count = 0
            if bin_rep[bit_index] == '1':
                count = 0
            while bin_rep[bit_index] == '0':
                if bit_index == len(bin_rep)-1 and bin_rep[bit_index] == '0':
                    count = 0
                    break
                count +=1
                bit_index +=1
            bin_gaps.append(count)
        else:
            bin_gaps.append(0)
    return bin_gaps

def solution(N):
    bin_rep = "{0:b}".format(N)
    bin_gaps = [0]
    for start_index in range(len(bin_rep)-1):
        if bin_rep[start_index] == '1':
            bit_index = start_index + 1
            count = 0
            if bin_rep[bit_index] == '1':
                count = 0
            while bin_rep[bit_index] == '0':
                if bit_index == len(bin_rep)-1 and bin_rep[bit_index] == '0':
                    count = 0
                    break
                count +=1
                bit_index +=1
            bin_gaps.append(count)
        else:
            bin_gaps.append(0)
    return max(bin_gaps)
