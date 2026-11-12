'''Diana is playing a game with two dice. One die has m sides labelled 1, 2, 3 ... m.
The other die has n sides labelled 1, 2, 3 ... n.
Write a program to determine how many ways can she roll the dice to get the sum 10.
For example, when the first die has 6 sides and the second die has 8 sides, there are 5 ways to get the sum :
2 + 8 = 10
3 + 7 = 10
4 + 6 = 10
5 + 5 = 10
6 + 4 = 10
'''

def dice_checker(m, n):
    count = 0
    first_die = 1

    while first_die <= m:
        second_die = 1

        while second_die <= n:
            if first_die + second_die == 10:
                count += 1
            second_die += 1

        first_die += 1

    return count

print(dice_checker(6, 10))