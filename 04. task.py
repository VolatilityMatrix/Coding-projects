import statistics
students_number = int(input())
mark_list = []
group1 = 0
group2 = 0
group3 = 0
group4 = 0
for a in range(students_number):
    mark_list.append(float(input()))
for mark in mark_list:
    if 2.00 <= mark <= 2.99:
        group1 += 1
    elif 3.00 <= mark <= 3.99:
        group2 += 1
    elif 4.00 <= mark <= 4.99:
        group3 += 1
    elif 5.00 <= mark:
        group4 += + 1

print(f"Top students: {((group4 / students_number) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((group3 / students_number) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((group2 / students_number) * 100):.2f}%")
print(f"Fail: {((group1 / students_number) * 100):.2f}%")
print(f"Average: {(statistics.mean(mark_list)):.2f}")