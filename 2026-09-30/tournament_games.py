win_amount = 0

for i in range(6):
    game = input("insert if your wins and losses: \n")
    if game == "w":
        win_amount += 1

print(f"you have {win_amount} wins")

if 5 <= win_amount <= 6:
    print("you are in group 1")
elif 3 <= win_amount <= 4:
    print("you are in group 2")
elif 1 <= win_amount <= 2:
    print("you are in group 3")
else:
    print("you are eliminated")