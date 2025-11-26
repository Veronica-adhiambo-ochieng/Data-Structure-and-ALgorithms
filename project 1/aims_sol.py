""""
In this problem, you will try your solution on three different datasets: small, medium, and large
To test your solution on each one of them run the following in the terminal,
for small: 
    python autograder.py -p aims -s small

for medium: 
    python autograder.py -p aims -s medium

for large: 
    python autograder.py -p aims -s large

"""

def aims(n, S):
    aims_set = {'a', 'i', 'm', 's'}
    transformed = [1 if char in aims_set else -1 for char in S]

    # Find the maximum subarray sum
    max_sum = 0
    current_sum = 0

    for value in transformed:
        current_sum = max(value, current_sum + value)
        max_sum = max(max_sum, current_sum)

    return max_sum


#################   DO NOT CHANGE BELOW ###########################

def run_code(name):
    fin = open(name, 'r')
    fout = open('datasets/aims/aims_sol.out', 'w')
    n_tests = int(fin.readline())
    for i in range(n_tests):
        n = int(fin.readline())
        S = fin.readline()[:-1]
        assert len(S) == n
        fout.write('%d\n' % aims(n, S))
    fin.close()
    fout.close()