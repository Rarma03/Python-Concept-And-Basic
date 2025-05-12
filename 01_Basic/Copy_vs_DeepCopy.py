import copy 

a = [ 1, [1,2], 3]
b = copy.copy(a) # alternate b = a[:]
c = copy.deepcopy(a)

a[1][0] = 55

print(a)
print("Shallow copy only outer level 1, Inner Level still have same reference :" , b)
print("Deep copy all level get new copied :" , c)