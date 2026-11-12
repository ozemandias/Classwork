def credit_card(num):
    percent_balance = num * 0.021
    if percent_balance >+ 10:
        return percent_balance
    else:
        return min(10, num)
    

