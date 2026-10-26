"""Create a function that prints the factors of the given positive integer argument.

Bonus, return the number of factors that argument has.
"""
def factors(num):
    if num < 1:
        return 0
    
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            print(f"{num} has a factor of {i}")
            total += 1
    return total

print(factors(24))