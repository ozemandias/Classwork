regular=4
large=6

number_regular = len(input("number of regular by typing r how ever many times \n"))
number_large = len(input("number of large by typing l how ever many times \n"))

price = float((regular*number_regular) + (large*number_large) * 1.13)
tip = float(input("tip in decimal \n"))
tip_percent = tip*100
total = price*(1+tip)

print (f"the total price is ${total} with a tip percentage of {tip_percent}%")
print (f"there are {number_regular} regular drinks and {number_large} large drinks")