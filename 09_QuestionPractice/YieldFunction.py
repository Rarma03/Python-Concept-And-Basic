# Yield used to return one value at a time, while remebering last return value
# Generally used in creating Generators, working with large datasets, streaming data, or pipelines

def even_generate(n):
    for num in range(2, n+1, 2):
        yield num

# yield also work as return in terms of exiting function

print(even_generate(10))        # 0x000002174D4202E0

for nums in even_generate(10):
    print(nums)

# if we use return instead of yield then 'even_generate' dont work as iterable object