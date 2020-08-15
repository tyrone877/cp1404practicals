out_file = open("name.txt", "w")
name = str(input("What is your name? ")).title()
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r+")
print(f"Your name is {name}")
in_file.close()

in_file = open("numbers.txt", "r")
numbers = in_file.readlines()
sum_of_first_two_lines = int(numbers[0]) + int(numbers[1])
print(sum_of_first_two_lines)
in_file.close()

in_file = open('numbers.txt', 'r')
total_of_all_values = 0
for line in in_file:
    total_of_all_values += int(line)
print(total_of_all_values)
in_file.close()
