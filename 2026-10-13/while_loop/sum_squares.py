def sum_of_squares():
    total = 0
    num = 2
    while total <= 200:
        total += num ** 2
        num += 1
        
    return total