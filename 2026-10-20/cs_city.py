"""2. In CS City, a mathematical place to live, the mayor is elected every 4 years, 
the treasurer is appointed every 2 years, the chief programmer is elected every 3 years 
and the dog-catcher is replaced every 5 years.

This year, Year 𝑋, the newly elected mayor announced the appointment of the new treasurer, 
a new dog-catcher and congratulated the chief programmer for winning the recent election.
That is, all positions were changed over. This is highly unusual. 
You will quantify how unusual this really is.
"""

def city(num, num2):
    current = 0
    while num <= num2:
        if current % 3 == 0 and current % 4 == 0 and current % 5 == 0:
            print(f"all positions change on {num}")    
        current += 1
        num += 1

city(2004, 2300)