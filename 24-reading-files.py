# Reading from files

# possible modes are 'r', 'w', 'r+', 'a'
employee_file = open('employees.txt', 'r')

# Check if file is readable
print(employee_file.readable())

# Read entire contents of file
print(employee_file.read())

# Read a single line
employee_file.seek(0)
print(employee_file.readline(), end='')
print(employee_file.readline(), end='')
print(employee_file.readline(), end='')

# Read all lines
employee_file.seek(0)
print(employee_file.readlines())

# Using a for loop
employee_file.seek(0)

for employee in employee_file.readlines():
    print(employee, end='')

# Make sure to always close the file
employee_file.close()