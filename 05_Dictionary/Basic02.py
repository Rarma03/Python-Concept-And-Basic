# looping in dictionary
sq_nums = {x:x**2 for x in range(10)}
print(sq_nums)

# multilayer dictionary
mp = {
    1 : {
        "name" : "raj",
        "place" : 'indore'
    },
    2 : {
        "name" : "rechal",
        "place" : 'rewa'
    }
}
print(mp[1]["name"])

# multilayer dict creation
ar1 = [1, 2, 3]
ar2 = ["Jan", "Feb", "Mar"]

mp = dict.fromkeys(ar1,ar2)
print(mp)   # output - {1: ['Jan', 'Feb', 'Mar'], 2: ['Jan', 'Feb', 'Mar'], 3: ['Jan', 'Feb', 'Mar']}

for ind in range(len(ar1)):
    mp[ar1[ind]] = ar2[ind]

print(mp)   # output - {1: 'Jan', 2: 'Feb', 3: 'Mar'}