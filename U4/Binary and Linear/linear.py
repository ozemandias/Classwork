from random import randrange, seed
seed(1)

test_list = []
for i in range(30):
    test_list.append(randrange(-100, 100))

test_list = sorted(test_list)
print(test_list)

# def linearsearch(data, target):
#     for i in test_list:
#         if i == target:
#             return target
#     return -1

def linearsearch(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

print(linearsearch(test_list, 95))