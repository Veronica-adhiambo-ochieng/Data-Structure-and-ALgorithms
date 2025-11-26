""""
In this problem, you will try your solution on two different datasets: small and large
To test your solution on each one of them run the following in the terminal,
for small: 
    python autograder.py -p mars -s small

for large: 
    python autograder.py -p mars -s large

    
Additionally, there's a third file called martian_example, which you do not need to test, you can use it to understand the problem better. 
"""
import math

def mars(day, month, year):
    # Define the days in months for regular and leap years
    regular_year_month_days = [28, 28, 28, 28, 28, 27, 28, 28, 28, 28, 28, 27,
                               28, 28, 28, 28, 28, 27, 28, 28, 28, 28, 28, 27]
    leap_year_month_days = [28, 28, 28, 28, 28, 27, 28, 28, 28, 28, 28, 27,
                            28, 28, 28, 28, 28, 27, 28, 28, 28, 28, 28, 28]

    # Helper function to check if a year is a leap year
    def is_leap_year(y):
        return y % 2 != 0 or y % 10 == 0

    # Validate inputs
    if not (1 <= month <= 24 and 1 <= year <= 10**9):
        return -1
    if is_leap_year(year):
        if not (1 <= day <= leap_year_month_days[month - 1]):
            return -1
    else:
        if not (1 <= day <= regular_year_month_days[month - 1]):
            return -1

    # Precompute necessary values
    year_offset = abs(year - 220)
    odd_years_count = year_offset // 2
    decades_count = (year // 10 - 220 // 10 - 1 if year > 220 else 
                     220 // 10 - year // 10 + (1 if year % 10 != 0 else 0))

    # Determine the total number of sols (days) based on year position
    if year <= 220:
        remaining_month_days = leap_year_month_days[month:] if is_leap_year(year) else regular_year_month_days[month:]
        remaining_sols = sum(remaining_month_days) + (leap_year_month_days[month - 1] - day if is_leap_year(year) else regular_year_month_days[month - 1] - day)
        total_sols = year_offset * 668 + odd_years_count + decades_count + remaining_sols
    else:
        completed_month_days = sum(leap_year_month_days[:month - 1]) if is_leap_year(year) else sum(regular_year_month_days[:month - 1])
        total_sols = (year_offset - 1) * 668 + odd_years_count + decades_count + completed_month_days + day

    # Compute the weekday
    if sols_count == 0:
        return 1
    elif year > 220:
        return (sols_count + 1) % 7
    else:
        if sols_count < 7:
            return (8 - sols_count) % 7
        else:
            return (8 - (sols_count % 7)) % 7

#################   DO NOT CHANGE BELOW ###########################

def run_code(name):
    fin = open(name, 'r')
    fout = open('datasets/mars/mars_sol.out', 'w')
    n_tests = int(fin.readline())
    for i in range(n_tests):
        d, m, y = map(int, fin.readline().split('.'))
        fout.write('%d\n' % mars(d, m, y))
    fin.close()
    fout.close()