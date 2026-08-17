students = []
passed = 0
failed = 0
total_score =0
highest_score =0
top_student = ''
while True:
    student_name = (input('Enter your name:'))
    score = float(input('Enter your score:'))

    if score <0 or score>100:
        print('invalid score number the score should be between 0 and 100')


        yes = (input('Do you want to continue? (y/n):'))
        if yes.lower() != 'y':
            break

        continue
    else:
         if score >= 90:
             grade= 'A'
         elif score >= 80:
             grade= 'B'
         elif score >= 70:
             grade= 'C'
         elif score >= 60:
             grade = 'D'
         else:
             grade = 'F'

    total_score += score
    if score > highest_score:
        highest_score = score
        top_student = student_name

    if score >= 60:
        status = 'passed'
        passed += 1
    else:
        status = 'failed'
        failed += 1


    print(f"Student:{student_name}")
    print(f"Score:{score}")
    print(f"Grade:{grade}")
    print(f"Status:{status}")

    students.append((student_name, score, grade, status))
    again = input('Do you want to continue? (y/n):')

    if again.lower() != 'y':
        break

print('\n All students')

for name,score,grade,status in students:
    print(f'Name:{name}, Score:{score}, Grade:{grade}, Status:{status}')

print(f'Total students:{len(students)}')
print(f'Total students passed:{passed}')
print(f'Total students failed:{failed}')



print(f'Tota score:{total_score}')
if len(students) >0:
    average_score = total_score/len(students)
    print(f'Average score: {average_score}')
else:
    print('No students recorded.')


print(f'Highest score:{highest_score}')
print(f'Student name:{top_student}')