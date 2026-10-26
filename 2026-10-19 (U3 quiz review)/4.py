"""Create a program that determines the numbers that are divisible 
by 7 and is a multiple of 5 between 1500 and 2700 inclusively."""

def something():
    total = 0
    current = 1500
    while current <= 2700:
        if current % 7 == 0 and current % 5 == 0:
            print(current)
        current += 1

something()