#Github Repo link : https://github.com/Kinley606/03230133_BIA101_CAP3
# Kinley Zangmo
# BBI A
# 03230133
#reference : https://realpython.com/python-exceptions/
#https://www.geeksforgeeks.org/built-exceptions-python/?ref=lbp
# Solution Score:488757


# Reading an input file using try-except block
def read_input(file_name): #The code defines a function named  that takes a single argument.
    try: #this code used to catch and handle exceptions (errors) that  occur during execution.
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError: #this code is executed when the specified file is not found.
        print(f"Error: File '{file_name}' is not found.")
        return []
    

# To calculate sum total of the two digit number.
def calculate_sum(lines):
    total_sum = 0
#The code iterates through each line in the input lines, extracts the first and last digits from the line and give total sum.   
    for line in lines: 
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            number = int(first_digit + last_digit)
            total_sum += number
    return total_sum

#This code will print the solution.
def print_solution(file_name):
    lines = read_input(file_name)
    total_sum = calculate_sum(lines)
    print(f"The total sum from the given input file {file_name} is {total_sum}")

#this line read the contents of the file, calculate the sum of the two-digit numbers, and print the result.
file_name = r'03230133_BIA101_CAPIII\\133.txt'
print_solution(file_name)