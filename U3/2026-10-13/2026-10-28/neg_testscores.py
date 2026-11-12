test = [-30, 43, -73, 35, 98, -26, -97, 20, 52, 73]
def test_checker(test):
    current_sum = 0
    for i in range(len(test) - 1 ):
        if test[0]:
        elif test[i] + test[i + 1] > current_sum:
            current_sum += i
        return current_sum