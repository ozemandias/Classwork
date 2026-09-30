first = int(input("what is the first grade? \n"))
second = int(input("what is the second grade? \n"))
third = int(input("what is the third grade? \n"))
fourth = int(input("what is the fourth grade? \n"))

average = (first+second+third+fourth)/4

if average < 80:
    print(f"your average is less than 80, it is {average}%")
elif 80 <= average < 90:
    print(f"you have an average of {average}% but you aren't eligible for a scholarship 80")
elif 90 <= average <= 94:
    print(f"you have an average of {average}% and you are eligible for a $2000 scholarship")
else:
    print(f"you have an avreage of {average}% and you are eligible for a $4000 scholarship")
