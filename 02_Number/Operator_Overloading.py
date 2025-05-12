# operator overloading means we are making same operator to add different things

a = 2 + 4

b = 'raj' + 'verma'

# above we did use + for addition of number then for string, operator automatically decides
# what are the data types it have left and right to it
print(a,b,a)

c = 2 + 'raj'       # it gives error
print(c)

d = 'raj' * 4
print(d)            # output - rajrajrajraj