# As list is mutable in nature we can change the value of object without creating a new one

# Example - 01
l1 = [1,2,3]
l2 = l1         # here we refrenced l2 to l1

print(l1)       # [1, 2, 3]
print(l2)       # [1, 2, 3]

l1[0] = 99

print(l1)       # [99, 2, 3]
print(l2)       # [99, 2, 3]

# Example - 02
p1 = [1,2,3]
p2 = p1         # we referenced

print(p1)       # [1, 2, 3]
print(p2)       # [1, 2, 3]

p2 = [1,2,3]    # removed referenced, create new obj

p1[0]=99

print(p1)       # [99, 2, 3]
print(p2)       # [1, 2, 3]