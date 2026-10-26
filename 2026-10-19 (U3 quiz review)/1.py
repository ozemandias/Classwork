''''1. Create a program that finds/prints the SUM OF SQUARES
    starting from 2 until the TOTAL SUM exceeds 200.'''

def sum_of_squares():
    start = 2
    sum = 0
    while sum <= 200:
        sum += (start**2)
        print(sum) 
        start += 1

sum_of_squares()