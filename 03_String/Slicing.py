num_list = "0123456789"

# no end limit
print(num_list[0:])         # output - 0123456789

# specific range
print(num_list[2:7])        # output - 23456

# hop count ( kitne chodna hain )
print(num_list[0:8:2])      # output - 0246

# negative

print(num_list[-1:])        # output - 9

print(num_list[:-1])        # output - 012345678

print(num_list[2:-4])        # output - 2345

print(num_list[-2:4])        # output - blank