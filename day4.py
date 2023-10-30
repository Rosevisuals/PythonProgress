# function to print asteriks in a descending order
# * * * * * * * * *
# ***
# **
# *

'''initial_asteriks = 9
num_rows = 5

def print_asteriks(initial_asteriks, num_rows):
    while (num_rows > 0):
        for i in range(initial_asteriks):
            print("*", end=" ")
            initial_asteriks -= 1
            if initial_asteriks == 0:
                break
        print("\n")
        num_rows -= 1
        initial_asteriks = num_rows
print("Enter number of initial asterisks: ")
initial_asteriks = int(input())

num_rows = int(input("Enter number of rows: "))

print_asteriks(initial_asteriks, num_rows)
'''


'''def add(a, b):
    print(a + b)

print("Enter numbers you want to add a and b")
a = int(input("Enter a: "))
b = int(input("Enter b: " ))
add(a, b)
    '''



'''def my_function():
   inner_variable = 42
   print(inner_variable)
def other_function():
   inner_variable = 20
   print(inner_variable)
my_function()		# This will print 42
other_function()     # This will print 20'''



'''def sayHello(name, message="Asalaam aleikum"):
    print(f"{message} {name}")


sayHello("Namubiru", message="Shallom")'''

# get the factorial of 5 - what do i do?
# 5 * 4 * 3 * 2 * 1 - factorial of 5 - 120
# 3 - 3 * 2 * 1

'''def factorial(num):
    if (num <= 1):
        return 1
    else:
        return num * factorial (num - 1)

num = int(input("Enter the number for which you want to determine the factorial: "))
print(factorial(num))'''

factorial = lambda num: print(num)
factorial(5)
    


# 5

