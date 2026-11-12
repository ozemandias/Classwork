"""# Let A be a list, N be a length of A
repeat until swapped is false
	swapped = false
	for i = 1 to N-1 (inclusively)
		if A[i-1] > A[i] then
			swap(A[i-1],A[i])
			swapped = true
"""
from random import randrange, seed
seed(1)

test_list = []
for i in range(5):
    test_list.append(randrange(-100, 100))

print(test_list)

def bubble_sort(A):
    N = len(A)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, N):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True

    return A

print(bubble_sort(test_list))

