from math import sqrt
def perfect_square(num):
    calculation = sqrt(num) % 1
    if calculation != 0:
        return False
    else:
        return True

print(f"Is 15 a perfect square?, {perfect_square(15)}")