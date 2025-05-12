def power(x):
    def calc(y):
        return y ** x
    return calc

sq = power(2)
cu = power(3)

print(sq(3))    # output - 9
print(cu(3))    # output - 27

# this is called as back-packing of function
# mostly used in django