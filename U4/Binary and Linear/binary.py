from random import randrange, seed
seed(1)

test_list = []
for i in range(30):
    test_list.append(randrange(-100, 100))

test_list = sorted(test_list)
print(test_list)

def binarysearch(data, target):
    n = len(data)
    left = 0
    right = n-1
    while left <= right:
        middle = (left + right)//2
        if data[middle] < target:
            left = middle + 1
        elif data[middle] > target:
            right = middle - 1
        else:
            return middle
    return -1

print(binarysearch(test_list, -1))