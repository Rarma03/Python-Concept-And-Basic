# Problem: Write a decorator that measures the time a function takes to execute

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} exec in {round(end - start + 1,3)}sec")

        return result
    
    return wrapper

@timer
def example(n):
    time.sleep(n)

example(3)