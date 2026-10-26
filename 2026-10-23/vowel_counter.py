def vowel_counter(word):
    count = 0
    for i in word:
        #if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        if i in "aeiou" or i in "AEIOU":
            count += 1

    return count

text = input("Enter a word: ")
print(f"{text} has {vowel_counter(text)} vowels.")

