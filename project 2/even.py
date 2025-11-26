#!/usr/bin/env python
# coding: utf-8
"""
To check if your solution is correct on a set run the following command(s) in terminal 

    python autograder.py -p even -s small

    python autograder.py -p even -s medium
    
    python autograder.py -p even -s large


run separately for each case
"""

import numpy as np

# def even_odd(): # Decide what arguments you want this to take
#     """
#     even_odd function 
#     takes as input one test case 
#     returns the solution for the test case (int)
#     """
#     # Write your Solution Here! 

#     raise NotImplementedError 

def even_odd(n, array):
    def merge_sort(array, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        violation = merge_sort(array, left, mid)
        violation += merge_sort(array, mid + 1, right)
        violation += merge(array, left, mid, right)

        return violation

    def merge(array, left, mid, right):
        B = []  
        current_left = left
        current_right = mid + 1
        my_even_count = 0
        sub_violation = 0

        while current_left <= mid and current_right <= right:
            if array[current_left] > array[current_right]:
                if array[current_right] % 2 != 0:
                    sub_violation += my_even_count
                B.append(array[current_right])
                current_right += 1
            else:
                if array[current_left] % 2 == 0:
                    my_even_count += 1
                B.append(array[current_left])
                current_left += 1

        while current_left <= mid:
            if array[current_left] % 2 == 0:
                my_even_count += 1
            B.append(array[current_left])
            current_left += 1

        while current_right <= right:
            if array[current_right] % 2 != 0:
                sub_violation += my_even_count
            B.append(array[current_right])
            current_right += 1

        # Overwrite the original array with merged results
        for i in range(len(B)):
            array[left + i] = B[i]

        return sub_violation

    return merge_sort(array, 0, len(array) - 1)



def run_code(in_name='datasets/small_even_odd_inversion.in'):
    """
    run_code function 
    takes one argument: the sample file to try
    loads the data and writes the solution to the output file (even_sol.out)
    """

    fin = open(in_name, 'r')                  # Do not change
    fout = open('datasets/even_sol.out', 'w')   # Do not change
    n_tests = int(fin.readline())
    for i in range(n_tests):
        n = int(fin.readline())
        A = list(map(int, fin.readline()[:-1].split(' ')))
        assert len(A) == n
        fout.write('%d\n' % even_odd(n, A))
    fin.close()
    fout.close()


