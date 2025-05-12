l = [1,2,3,4]

I = iter(l)

print(I)                # 0x000001D946D3AEF0
print(I.__next__())     # 1
print(I)                # 0x000001D946D3AEF0
print(I.__next__())     # 2
print(I)                # 0x000001D946D3AEF0
print(I.__next__())     # 3
print(I)                # 0x000001D946D3AEF0
print(I.__next__())     # 4
print(I)                # 0x000001D946D3AEF0
print(I.__next__())     # error - 'StopIteration'

# iter always point to the start location, but save the last point uptill it read
# internal pointer remember the last read point