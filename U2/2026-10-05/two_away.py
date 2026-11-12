def two_away(num):
    final_result = num % 10 
    if final_result == 2 or final_result == 8:
        return True
    else:
        return False

print(f"is 18 two away from ten? {two_away(18)}")