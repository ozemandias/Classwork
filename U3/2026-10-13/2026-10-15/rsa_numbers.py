def rsa_checker(start, end):
    rsa_count = 0

    while start <= end:
        divisor_count = 0
        i = 1

        while i <= start:
            if start % i == 0:
                divisor_count += 1
            i += 1

        if divisor_count == 4:
            rsa_count += 1

        start += 1

    return rsa_count

