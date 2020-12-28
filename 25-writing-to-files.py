employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# Appending
employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

# Overwrite file
employee_file = open("employees1.txt", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()