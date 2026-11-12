def scrabble(string):
    points = 0
    string = string.lower()
    for i in string:
        if i in "eaionrtlsu":
            points += 1
        elif i in "dg":
            points += 2
        elif i in "bcmp":
            points += 3
        elif i in "fhvwy":
            points += 4
        elif i == "k":
            points += 5
        elif i in "jx":
            points += 8
        elif i in "qz":
            points += 10
    return points

print(scrabble("qweasdjkluoi"))