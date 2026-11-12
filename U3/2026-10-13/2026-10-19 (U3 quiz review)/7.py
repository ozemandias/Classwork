"""If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Create a program that finds the sum of all the multiples of 3 or 5 below 1000
Improve the program so that it finds the sum of all the 
multiples of 3 or 5 below N where N is greater than 5.
"""

def natural(num):
    current = 5
    while current < num:
        if current % 3 == 0 or current % 5 == 0:
            print(current)
        current += 1

natural(10)