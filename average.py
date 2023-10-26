num_subjects = int(input("Enter the number of subjects: "))
marks_list = []

count = 0
sum = 0
average = 0

while ( count < num_subjects):
    subject_mark = int(input("Enter the mark for the subject: "))

    if ((subject_mark >= 0 and subject_mark <= 100)):
        marks_list.append(subject_mark)
        sum += subject_mark
        count += 1
    else:
       print("Invalid mark. Marks should be between 0 and 100.")  
       
    average = sum / num_subjects

if (average > 90):
    grade = 'A'
elif (average > 80):
    grade = 'B'
elif (average > 70):
    grade = 'C'
elif(average > 60):
    grade = 'D'
else:
    grade = 'F'

print("This is the list of the marks: ", marks_list)    

print(f"The average is {average} and the grade is {grade}")