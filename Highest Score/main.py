student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
maximum = 0
score=0
for highest_score in student_scores:
    if highest_score > maximum:
        maximum = highest_score
    else:
        pass
print(maximum)
