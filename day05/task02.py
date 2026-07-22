student_score = [150, 142, 185, 128, 24, 59, 68, 199, 65, 80, 300, 1]

# total_exam_score = sum(student_score)

# print(total_exam_score)

# sum = 0

# for score in student_score:
#     sum += score

# print(sum)

print(max(student_score))

max = 0
for num in student_score:
    while max < num:
        max = num
    # if num > max:
    #     max = num

print(max)