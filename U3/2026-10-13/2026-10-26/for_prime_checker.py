"""Prime Checker.
A prime number is a number greater than 1 that only has two factors, 1 and itself.
A non prime number is considered a composite number.

7 is a prime number while 8 is a composite number.
Create function that returns True for primes and False for Composite
"""

def prime_checker(num):
    total = 0
    if num < 2:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0:
        return False
    else:
        upper_limit = int(num ** 0.5)+1
        for i in range(3, upper_limit, 2):
            if num % i == 0:
                return False
        return True

def poopoo(bum):
    for i in range(1, bum+1):
        print(prime_checker(i),i)
        
poopoo(int(input("input number please:\n")))