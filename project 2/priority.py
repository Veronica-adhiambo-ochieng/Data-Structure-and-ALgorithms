#!/usr/bin/env python
# coding: utf-8
"""
To check if your solution is correct on a set run the following command(s) in terminal 

    python autograder.py -p priority -s small
    
    python autograder.py -p priority -s large


run separately for each case
"""
# import numpy as np

class PriorityQueue:
    def __init__(self):
        self.array = []

    @staticmethod
    def parent(ind):
        return (ind - 1) // 2

    @staticmethod
    def left(ind):
        return 2 * ind + 1

    @staticmethod
    def right(ind):
        return 2 * ind + 2

    def even_leaves(self):
        n = len(self.array)
        count = 0

        if n == 0:
            return 0
        
        for i in range(n):
            if self.left(i) >= n and self.right(i) >= n:  # Check if it's a leaf
                if self.array[i] % 2 == 0:  # Check if the leaf is even
                    count += 1
        return count

    def fix_heap(self, ind):
        n = len(self.array)
        left = PriorityQueue.left(ind)
        right = PriorityQueue.right(ind)
        largest = ind

        if left < n and self.array[left] > self.array[largest]:
            largest = left
        if right < n and self.array[right] > self.array[largest]:
            largest = right

        if largest != ind:
            self.array[ind], self.array[largest] = self.array[largest], self.array[ind]
            self.fix_heap(largest)

    def extract_maximum(self):
        n = len(self.array)
        if n == 0:
            return
       
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.array.pop()  
        self.fix_heap(0)  

    def insert(self, x):
        self.array.append(x)
        ind = len(self.array) - 1
        while ind > 0 and self.array[ind] > self.array[PriorityQueue.parent(ind)]:
            parent = PriorityQueue.parent(ind)
            self.array[ind], self.array[parent] = self.array[parent], self.array[ind]
            ind = parent


Queue = PriorityQueue()

def priority(n, array):
    """
    Takes as input one test case returns a list of integers for each 'E' operation's output
    """
    global Queue
    results = []  
    skip = 0
    
    for i in range(len(array)):
        if skip > 0:  
            skip -= 1
            continue

        operation = array[i]
        if operation == 'I':  
            Queue.insert(int(array[i + 1]))
            skip = 1  
        
        elif operation == 'M':  
            Queue.extract_maximum()
        
        elif operation == 'E':  
            results.append(Queue.even_leaves())

    Queue = PriorityQueue()  
    return results  



def run_code(in_name='datasets/priority_small.in'):
    """
    run_code function 
    takes one argument: the sample file to try
    loads the data and writes the solution to the output file (priority_sol.out)
    """

    fin = open(in_name, 'r')                  # Do not change
    fout = open('datasets/priority_sol.out', 'w')   # Do not change

    k = int(fin.readline())  
    for i in range(k):
        n = int(fin.readline())  
        array = []
        for j in range(n):
            array.extend(fin.readline().strip().split(' '))


        results = priority(n, array)
        # print(results)
        for res in results:
            fout.write(f'{res}\n')  

    fin.close()
    fout.close()
    # raise NotImplementedError 


