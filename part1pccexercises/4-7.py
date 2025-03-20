#Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
multiples_of_3 = []


for num in range(3, 31, 3):
    multiples_of_3.append(num)
print(multiples_of_3)


# multiples=[value*3 for value in list1]      list comprehension:creates a list in one line of code
# print(multiples) 