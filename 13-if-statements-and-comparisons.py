# Comparison Operators Examples

# More info: https://www.tutorialsteacher.com/python/python-comparison-and-logical-operators

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def string_is_equal(s1, s2):
    if s1 == s2:
        return 'is_equal'
    else:
        return 'not_equal'


print(max_num(3, 4, 5))
print(max_num(30, 4, 5))
print(max_num(3, 40, 5))

print(string_is_equal("dog", "dog"))
print(string_is_equal("dog", "cat"))