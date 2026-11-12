day = int(input("what day of the week is it in interger format"))

if day == 1 or day == 7:
    print("the party is successful")
    exit()

acorn = int(input("number of acorns"))

if 40 <= acorn <= 60:
    print("the party is successful")
else:
    print("the party is not successfull")