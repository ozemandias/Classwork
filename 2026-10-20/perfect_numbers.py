"""The proper divisors of a number are the factors of a number that is not equal to itself.

Example → 12 has the proper divisors of: 1, 2, 3, 4, 6.

A perfect number is defined when the sum of a number’s proper 
divisors equal to the number itself.

Find the total sum of perfect numbers under 10,000.
"""

def divisors(num):
    total = 0
    divider = 1
    while divider < num:
        if num % divider == 0:
            total += divider
        divider += 1

    return num == total


values = 2
while values <= 10000:
    if divisors(values):
        total_sum += values
    values += 1
print(total_sum)