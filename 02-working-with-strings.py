# Example of newline in string
print("Giraffe\nAcademy")

# Example of escaping double-quote
print("Giraffe\"Academy")

# Escape backslash
print("\\")

# Variable assignment
phrase = "Giraffe Academy"
print(phrase)

# Concatenation (appending)
print(phrase + " is cool")

# Functions to modify string
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())

# Function Chaining
print(phrase.upper().isupper())

# Length of string
print(len(phrase))

# Get individual characters of string, 0-based indexing
print(phrase[0])

# The index function. Below will be 11
print(phrase.index('de'))

# This throws an error because there is no 'z'
#print(phrase.index('z'))\

# String.replace method
print(phrase.replace("Giraffe", "Tiger"))