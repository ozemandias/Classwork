def date(month, day):
    if month == 2 and day == 18:
        return "special"
    else:
        if month <= 2 and day < 18:
            return "before" 
        elif month < 2 and day > 18:
            return "before"
        elif month >= 2 and day > 18:
            return "after"
        else:
            return "after"

print(date(3, 2))