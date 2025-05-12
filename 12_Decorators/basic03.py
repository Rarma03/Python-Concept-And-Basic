import time

def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args, **kwargs):
        if args not in cache_value:
            res = func(*args, **kwargs)        
            print(args)
            cache_value[args] = res

        return cache_value[args]

    return wrapper

@cache
def long_running_func(a, b):
    time.sleep(4)
    return a+b
# -- OR --
@cache
def long_running_func(*args):
    time.sleep(4)
    return sum(args)

print(long_running_func(2,3))
print(long_running_func(3,3))
print(long_running_func(2,3))
print(long_running_func(2,3,5))
print(long_running_func(2,3,5))