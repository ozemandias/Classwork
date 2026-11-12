telemarketer = list(input("last four numbers: \n"))

if telemarketer[0] in {'8', '9'}:
    if telemarketer [-1] in {'8', '9'}:
        if telemarketer [1] == telemarketer [2]:
            print("this is a telemarketer number")
        else:
            print("this is not a telemarketer number")
    else:
        print("this is not a telemarketer number")
else: 
    print("this is not a telemarketer number")