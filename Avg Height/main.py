student_heights = input("Input a list of student heights ").split(" ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total = 0
for students in student_heights:
    height = students
    total += height
print(total)
count = 0
for number in student_heights:
    count += 1
print(count)
avg_height = round(total / count)
print(avg_height)
