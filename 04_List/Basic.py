y = ['Jan', 'Feb', 'March', 'April']

# looping and printing
for val in y:
    print(val)

for val in y:
    print(val, end=' ')     # bydefault end = "\n"

# insert at last position
y.append("May")
print(y)

# insert at any position
y.insert(1,"Feb")
print(y)

# remove last value
y.pop()
print(y)

# remove any value
y.remove("Feb")
print(y)

# referencing vs copy
x = y           # we referenced the same object in memory

x = y.copy()    # we created new object, copying all data