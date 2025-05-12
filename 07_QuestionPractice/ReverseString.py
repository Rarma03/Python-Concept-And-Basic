s = input("Enter the string: ")

rev = ""

# range(start, stop, step)
for ind in range(len(s)-1, -1, -1):
    rev += s[ind]

print(rev)

# positive traversal : for ind in range(0, n, 1)
# negative traversal : for ind in range(n-1, -1, -1)