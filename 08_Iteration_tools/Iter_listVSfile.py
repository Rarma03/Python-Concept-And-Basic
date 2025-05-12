f = open(r'D:\Python - Learning\08_Iteration_tools\readablefile.py')

l = [1, 2, 3, 4]

print(f is iter(f)) # True
print(l is iter(l)) # False