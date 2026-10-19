'''FizzBuzz is counting from 1 to 50 and outputing the number; however, certain numbers will output fizz, buzz or fizzbuzz.

if the number is a multiple of three: print 'Fizz',
if the number is a multiple of five: print 'Buzz',
if they are multiples of both: print 'FizzBuzz'
otherwise print the number'''

def num():
    current = 1
    while current <= 50:
        if (current % 3 == 0) and (current % 5 == 0):
            print("Fizzbuzz")
        elif current % 3 == 0:
            print("Fizz")
        elif current % 5 == 0:
            print("Buzz")
        else:
            print(current)
        current += 1

num()