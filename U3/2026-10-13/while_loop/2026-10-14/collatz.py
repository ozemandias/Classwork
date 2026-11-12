def collatz(num):
    counter = 1
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        counter += 1
    return counter
collatz(23)