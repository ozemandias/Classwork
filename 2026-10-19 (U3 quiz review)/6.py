"""Create a program that outputs the square of N and the cube of N 
of all numbers from 2 to N, where N is the user input, type integer, greater than 2.

Output N = 3

2 4 8
3 9 27
"""

def something(num):
    current = 2
    while current <= num:
        square = current ** 2
        cube = current ** 3
        print(current, square, cube)
        current += 1

something(5)