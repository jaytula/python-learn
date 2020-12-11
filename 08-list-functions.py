lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Tim"]
friends_copy = friends.copy()

# Printing out a list
print(friends)

# Extend function
friends_copy.extend(lucky_numbers)
print(friends_copy)

# Appending an item
friends.append('Creed')
print(friends)

# Insert
friends.insert(1, "Kelly")
print(friends)

# Remove
friends.remove("Jim")
print(friends)

# Pop - removes last item from list
friends.pop()
print(friends)

# Index - returns the index of the found item
kevin_index = friends.index("Kevin")
print(kevin_index)

# Count elements
jim_count = friends.count("Jim")
print(jim_count)

# Sort list
friends.sort()
print(friends)

# Reverse a list
friends.reverse()
print(friends)

# Remove all items
friends.clear()
print(friends)