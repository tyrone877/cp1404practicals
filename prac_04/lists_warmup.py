"""
What values do the following expressions have?

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] = [1]
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


"""
numbers = [3, 1, 4, 1, 5, 9, 2]
#  Change the first element of numbers to "ten" (the string, not the number 10)

numbers[0] = "ten"
print(numbers)

#  Change the last element of numbers to 1

numbers[-1] = 1
print(numbers)

#  Get all the elements from numbers except the first two (slice)

new_numbers = numbers[1:-1]
print(new_numbers)

#  Check if 9 is an element of numbers
print((9 in numbers))
