def scrabble(words):
    points = 0
    words = words.lower()
    for i in words:
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

def best_scrabble(text):
    top_score = 0
    top_word = ""

    for words in text:
        current_score = scrabble(words.upper)

        if current_score > top_score:
            top_score = current_score
            top_score = words
    return top_score

words = [
    "perspective"
    "menu"
    "uncle"
    "contract"
    "airport"
    "story"
    "safety"
    "basket"
    "photo"
    "advertising"
    ]