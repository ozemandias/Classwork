"""3. Create a program that asks for 10 floating point numbers; 
calculate the total sum, total product, and average of the 10 numbers."""

tsum = 0
tpro = 1
average = 0
count = 0
while count < 10:
    count += 1
    current = float(input("number here:"))
    tsum += current
    tpro *= current
    current = 0
average = (tsum/10)

print(f"the total sum is {tsum}")
print(f"total product is {tpro}")
print(f"the average is {average}")