def number_factor(num):
    divisor = 1
    while divisor <= num:
        if num % divisor == 0:
            print(divisor)
        divisor += 1

number_factor(352)