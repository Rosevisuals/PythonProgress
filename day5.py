# Python Lists

'''my_list = ["Betty", "Samson", "Brian"]
print(type(my_list))'''

'''my_list = list()
print(type(my_list))
my_list.append("Betty")
my_list.append("Samson")
my_list.append("Brian")

print(len(my_list))'''



'''count = 0
list_int = list()

while (count < len(my_list)):
# for element in my_list:
    if (type(my_list[count]) == int):
            list_int.append(my_list[count])
    count += 1
    


print(list_int)'''

'''my_list = [1, 2, 3, 'Adam', 'Bright', 4, 5]
my_list.insert(4, 6)
print(my_list)
print(my_list[1:4])

# Simple Exercise on list methods
# 1. Create a list of 5 elements
# 2. Add 2 more elements to the list
# 3. Remove the 3rd element from the list
# 4. Print the list'''

'''nums = [1, 2, 3, 4]
names = ['micheal', 'micheal', 'sam']
names.extend(nums)
combined_list = nums.extend(names)
# an_combined_list = nums + names
print(names)
# print(nums)
# print(combined_list)
# print(an_combined_list)'''


'''num_list = [1, 2, 3, 4, 5]
num_list.pop(2) # for pop method you specify the index
print(num_list )'''

num_list = [1, 2, 3, 4, 5]
'''

# remove method - specify the item
# clear - empty the list

print(num_list)'''

copy_list = num_list.copy()
copy_list.sort(reverse=True)
print(copy_list)









