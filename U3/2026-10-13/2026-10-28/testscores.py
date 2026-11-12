test = [30, 43, 73, 25, 98, 26, 97, 20, 52, 73]
def test_avg(marks):
    average_grade = 0
    total = 0
    for i in range(len(marks)):
        total += marks[i]
    average_grade = total / len(marks)
    
    return average_grade

print(f"{test} has an average of {test_avg(test)}%")