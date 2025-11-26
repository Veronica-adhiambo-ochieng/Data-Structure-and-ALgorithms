
""""
To test your solution run the following in the terminal: 
    python autograder.py -p entropy
"""
import numpy as np
import math
def entropy(alpha):

    #   Write your solution here!
    # The preprocessing is already done for you, implement your algorithm here, you're given one input case at a time through this function.
    # return result
    # raise NotImplementedError
    if alpha == 0:
        return 0.0
    if alpha == 1:
        return 0.5

    # Define the binary entropy function
    def entropy(p):
        if p == 0 or p == 1:
            return 0
        return -p * math.log2(p) - (1 - p) * math.log2(1 - p)

    # Binary search
    low, high = 0, 0.5
    while high - low > 1e-7:  # Precision >= 10^-6
        mid = (low + high) / 2
        if entropy(mid) < alpha:
            low = mid
        else:
            high = mid

    return (low + high) / 2  # Return the midpoint


#################   DO NOT CHANGE BELOW ###########################
INPUT_NAME = 'datasets/entropy/entropy.in'
OUTPUT_NAME = 'datasets/entropy/entropy_sol.out'
def run_code():
    f = open(INPUT_NAME, 'r')
    
    fout = open(OUTPUT_NAME, 'w')
    
    n_tests = int(f.readline())
    for i in range(n_tests):
        alpha = float(f.readline())
        p_str = entropy(alpha)
        fout.write(str(p_str) + '\n')
    f.close()
    fout.close()







