#!/usr/bin/env python
# coding: utf-8
"""
To check if your solution is correct on a set run the following command(s) in terminal 

    python autograder.py -p connections -s small
    
    python autograder.py -p connections -s large


run separately for each case
"""

import numpy as np



#def close_connections(): # Decide what arguments this function should take
    #"""
  #  close_connections function 
#    takes as input one test case 
  #  returns the solution for the test case (int)
   # """
    # Write your Solution Here! 

  #  raise NotImplementedError 



# call deque and default dictionary
from collections import defaultdict, deque

#import numpy as np

# define a function
def count_close_connection(n, m, s, k):
    """ count the number of reacheable vertices provided number of k steps from point s"""
    visited = [False] * (n + 1)
    Queue = deque([(s, 0)])
    visited[s] = True
    points_count = 0

    while Queue:
        vertex, steps = Queue.popleft()
        points_count += 1
        if steps == k:
            continue
        # traversing neighbours
        for neighbour in m[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                Queue.append((neighbour, steps + 1))
    return points_count

def close_connection(test_sets):
    """ Identifying the close connection to s"""
    results = []
    for case in test_sets:
        n, m, s, k = case["params"]
        edges = case["edges"]
        topology = defaultdict(list)  

        for a, b in edges:
            topology[a].append(b)

        results.append(count_close_connection(n, topology, s, k))
        #print(results)
    return results



def run_code(in_name='datasets/connections_small.in'):
    """
    run_code function 
    takes one argument: the sample file to try
    loads the data and writes the solution to the output file (connections_sol.out)
    """
    fin = open(in_name, 'r')                  # Do not change
    fout = open('datasets/connections_sol.out', 'w')   # Do not change


    with fin:
        test_cases = int(fin.readline().strip())
        test_sets = []
        
        for _ in range(test_cases):
            n, m, s, k = map(int, fin.readline().strip().split())
            edges = [tuple(map(int, fin.readline().strip().split())) for _ in range(m)]
            test_sets.append({"params": (n, m, s, k), "edges": edges})
    
    # Process test cases
    results = close_connection(test_sets)
    
    # Write results to output file
    with fout:
        fout.write('\n'.join(map(str, results)) + '\n')


    fin.close()
    fout.close()

    #raise NotImplementedError 




