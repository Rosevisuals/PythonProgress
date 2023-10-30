'''# temp = 30.5
# deg = "C"

# Program to convert from Fahrenheit to Celsius and vice versa

print("Enter the degree: ")
deg = str(input())

print("Enter the temperature: ")
temp = float(input())


if deg == 'C':
    print("Temperature in Fahrenheit is: ", (temp * 1.8) + 32)
elif deg == 'F':
    print("Temperature in Celsius is: ", (temp - 32) / 1.8)'''

'''x = 5
x ** 4 # 2 to the power 4
print(x ** 4)


print(x // 2)'''


'''x = 20

x += 5
print(x)

x -= 5 # x = x - 5
print(x)'''

# Comparison Operators

'''print(5 == 5)

x = 20
y = 4

if (x != y):
    print("x is not equal to y")
else:
    print("x is equal to y")
'''

'''username = str(input("Enter your username: "))
pin = int(input("Enter your pin: "))   

if (username.lower() == "elisa" or pin == 1234):
    print("You are allowed to access your account")
else:
    print("You are not allowed to access your account")'''

'''x = 5
y = 5

print(x is y)'''

'''name = "Aliddeki"
if 'a' in name:
    print('There is an a in the name')
else:
    print('There is no a in the name')'''

'''# Lists
employee_list = str(input("Enter the names of the employees: "))
employee_age = int(input("Enter the age of the employees: "))
employee_age = employee_age.split()
employee_list = employee_list.split()
# count the number of employees in the list
# len method - count the no of string

if (len(employee_list == 5)):
    if (employee_age > 20):
        print("{}You are allowed to work in the company")
        '''

#count = 10

'''while (count <= 10):
    print(count) 
    count += 1'''

'''while (count >= 0):
    print(count)
    count -= 1'''


# Create a while loop to print the first 10 even numbers and add them

# Program to print first 5 even numbers and their sum

#count = 0
'''sum = 0

while (count <= 10):
    sum += count
    count += 2
    print(count)
    
print(f"The sum is {sum}")'''


'''
fruits = ['apples', 'oranges', 'mangoes']
for x in fruits:
    print(x)


sum = 0
num_list = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for num in num_list:
    if (num % 2 == 0):
        print(num)
        sum += num

print(f"The sum of the first 5 even numbers is {sum}")
'''
num_subjects = int(input("Enter the number of subjects: "))
marks_list = []

count = 0
sum = 0
average = 0

while count < num_subjects:
    subject_mark = int(input("Enter the mark for the subject: "))
    
    if 0 <= subject_mark <= 100:
        marks_list.append(subject_mark)
        sum += subject_mark
        count += 1
    else:
        print("Invalid mark! Please enter a mark between 0 and 100.")
       
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





   







