"""Given an integer input greater than 0, print all its factors. 
Output for N = 12
1
2
3
4
6
12
"""

def factor_finder(num):
    divisor = 1
    while divisor <= num:
        if num % divisor == 0:
            print(divisor)
        divisor += 1

factor_finder(24)