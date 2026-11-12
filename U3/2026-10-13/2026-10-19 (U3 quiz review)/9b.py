"""Create a program that lists all prime numbers under N, 
an integer input that is greater than 2."""

def prime(num):
    divisor = 2
    count = 0
    while divisor < num and count == 0:
        if num == 2:
            print("prime")
            count += 1
        elif num % divisor == 0:
            print("not a prime")
            count += 1
        divisor += 1
    if count == 0:
        print("prime")
            

prime(1009)