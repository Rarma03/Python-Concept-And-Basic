# same as maps in C++

mp = {
    1 : "Luffy",
    2 : "Goku",
    3 : "Naruto",
    4 : "Gamify"
}

# printing whole map
# 1. normal print
print(mp)

# 2. loop print
for key,value in mp.items():
    print(key, value)

# printing key value single
print(mp[1])

# getting length
print(len(mp))

# remove key
mp.pop(4)
print(mp)

del mp[3]
print(mp)
# -> difference between del and pop is that pop returns a value which is removed [ same as queue in c++]

# adding is also similar to map
mp[5] = 4       # yeah! this works
print(mp)