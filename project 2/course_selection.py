#!/usr/bin/env python
# coding: utf-8
"""
To check if your solution is correct on a set run the following command(s) in terminal 

    python autograder.py -p course -s small
    
    python autograder.py -p course -s large


run separately for each case

If you get an error: Segmentation Fault, run this command:

    ulimit -s unlimited 


"""
from collections import defaultdict, deque
#import numpy as np
import sys 
sys.setrecursionlimit(100000000)


def course_selection(n, m, constraints): # Decide what arguments this function should take
    """
    course_selection function 
    takes as input one test case loaded from the .in file
    returns the solution for the test case (list, or if there's no possible solution return str(IMPOSSIBLE))
    """
    # Write your Solution Here! 

    #raise NotImplementedError 

    # Create adjacency list and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for a, b in constraints:
        graph[a].append(b)
        in_degree[b] += 1

    # Initialize queue with nodes having in-degree of 0
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles (if the result doesn't include all courses)
    if len(result) != n:
        return "Impossible"

    return " ".join(map(str, result))


def process_test_cases(test_cases):
 
    results = []
    for n, m, constraints in test_cases:
        results.append(course_selection(n, m, constraints))
    return results



def run_code(in_name='datasets/course_selection_small.in'):

    fin = open(in_name, 'r')  # Do not change
    fout = open('datasets/course_sol.out', 'w')  # Do not change

    with fin:
        test_cases = int(fin.readline().strip())
        test_sets = []

        for _ in range(test_cases):
            n, m = map(int, fin.readline().strip().split())
            constraints = [tuple(map(int, fin.readline().strip().split())) for _ in range(m)]
            test_sets.append((n, m, constraints))

    # Process test cases
    results = process_test_cases(test_sets)

    # Write results to output file
    with fout:
        fout.write("\n".join(results) + "\n")

    fin.close()
    fout.close()

   
