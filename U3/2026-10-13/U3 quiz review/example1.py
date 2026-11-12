def length(words):
    shortest = len(words[0])
    longest = len(words[0])
    total = 0
    for i in words:
        if shortest > len(i):
            shortest = len(i)
        
        if longest < len(i):
            longest = len(i)

    total = longest * shortest
    return total


























def length(words):
    longest = len(words[0])
    shortest = len(words[0])
    total = 0
    for i in words:
        if len(i) > longest:
            longest = len(i)

        if len(i) < shortest:
            shortest = len(i)
    total = shortest * longest
    return total

print(length(["pee", "poopoo", "lalala"]))