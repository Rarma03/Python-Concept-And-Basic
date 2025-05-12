# Arithmetic Operators
a = 10 + 5       # Addition
b = 10 - 5       # Subtraction
c = 10 * 5       # Multiplication
d = 10 / 3       # Division (float)
e = 10 // 3      # Floor Division (int)
f = 10 % 3       # Modulus (remainder)
g = 2 ** 1000    # Exponentiation 

# Comparison Operators
h = (10 == 5)    # Equal
i = (10 != 5)    # Not Equal
j = (10 > 5)     # Greater Than
k = (10 < 5)     # Less Than
l = (10 >= 5)    # Greater or Equal
m = (10 <= 5)    # Less or Equal

# Logical Operators
x = True and False   # Logical AND
y = True or False    # Logical OR
z = not True         # Logical NOT

# Bitwise Operators
p = 5 & 3       # AND
q = 5 | 3       # OR
r = 5 ^ 3       # XOR
s = ~5          # NOT
t = 5 << 1      # Left Shift
u = 5 >> 1      # Right Shift

# Assignment Operators
n = 5
n += 2          # Same as n = n + 2
n -= 1
n *= 2
n /= 3
n %= 2
n //= 1
n **= 2
n &= 1
n |= 2
n ^= 3
n <<= 1
n >>= 1

# Identity Operators
v = [1, 2]
w = v
x1 = v is w         # True (same object)
x2 = v is not [1,2] # True (different object despite same content)

# Membership Operators
y1 = 2 in [1, 2, 3]     # True
y2 = 4 not in [1, 2, 3] # True