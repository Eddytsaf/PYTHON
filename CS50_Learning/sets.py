# Create an empty set
s = set()

# Add elements to set
# set() method does not allow you to appear an element twice in a list
s.add(1)
s.add(2)
s.add(2)
s.add(3)
s.add(4)
print(s)

# Remove an element
s.remove(3)
print(s)

# len is use to calculate the number total of elements in a list
print(f"The set has {len(s)} elements")

