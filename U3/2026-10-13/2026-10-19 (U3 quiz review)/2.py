"""2. Create a program that adds all the numbers from 1 to User Input of a value.
"""

def something(num):
    start = 1
    total = 0
    while num >= start:
        total += start 
        start += 1
    print(total)

something(67)