# LEARN TO PASS MULTIPLE VALUES I.E. ANY NUMBER OF AMOUNT

# basic we use array/list to pass multiple values
def func(l):
    print(l)

func([1,2,3,4])

# BUT, BUT what if you dont want to pass array ?
# python provides *args to achive passing multiple paramater without defining them in function
def func1(*args):
    print(args)     # output - (1, 2, 3, 4)  i.e. tupple
    print(*args)    # output - 1 2 3 4
    return True

func1(1,2,3,4)

# There is another version of passing multiple paramerter - i.e. **kwargs
def func2(**kwargs):
    for key, value in kwargs.items():
        print(key,value)

func2(name='raj', surname='verma', dob='07/10/2002', gender='male-sigma')