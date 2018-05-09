
def  marks_avg_diff(marks):
    avg = sum(marks) // len(marks)
    diff = []
    for m in marks:
        diff.append( (m, m - avg))

    return diff


marks = [67,88,67,98,99,79,77,45]
print (marks_avg_diff(marks))



