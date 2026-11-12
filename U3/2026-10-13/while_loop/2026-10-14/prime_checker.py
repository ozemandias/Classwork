def prime(num):
    if num < 2:
         return False
    elif num == 2:
        return True
    else:
        divider = 2
        while divider < num:
            if num % divider == 0:
                return False
            divider += 1
        return True