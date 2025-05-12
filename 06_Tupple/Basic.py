# Major difference between List and Tuple:
# - Lists are mutable: you can change contents
# - Tuples are immutable: can't change once created

# 1. Creating tuples
month = ("Jan", "Feb", "Mar", "Apr")
more_month = ("May", "Jun")

# 2. Concatenating tuples (can also be done in lists)
nw = month + more_month
print("Concatenated:", nw)

# 3. Conditional check
if "Mar" in month:
    print("Yes, Mar is present")

# 4. Count occurrences
print("Count of 'Oct':", month.count("Oct"))

# 5. Nested tuples
nes = (1, (2, 3), 4)
print("Nested tuple:", nes)

# 6. Index of element
print("Index of 'Apr':", month.index("Apr"))

# 7. Tuple unpacking
a, b, c = ("Red", "Green", "Blue")
print("Unpacked:", a, b, c)

# 8. Single element tuple — must use comma
single_wrong = ("Jan")       # Not a tuple
single_right = ("Jan",)      # This is a tuple
print("Type check:", type(single_wrong), type(single_right))

# 9. Tuple used as dictionary keys
coordinates = {(0, 0): "Origin", (1, 2): "Point A"}
print("Dict with tuple keys:", coordinates[(1, 2)])

# 10. Tuple with mutable elements
t = ([1, 2], [3, 4])
t[0].append(99)              # Changing list inside tuple
print("Mutable inside tuple:", t)

# 11. Tuple functions
numeric_tuple = (4, 1, 3)
print("Length:", len(numeric_tuple))
print("Max:", max(numeric_tuple))
print("Min:", min(numeric_tuple))
print("Sum:", sum(numeric_tuple))

# 12. Memory efficiency
import sys
lst = [1, 2, 3]
tup = (1, 2, 3)
print("List size:", sys.getsizeof(lst))
print("Tuple size:", sys.getsizeof(tup))