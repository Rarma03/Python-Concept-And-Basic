# Learned to return multiple values & setting default value of function parameters
import math

def calc(r = 0):        # 0 is used as default if no r is provided
    return 2 * math.pi * r , math.pi * (r ** 2)

if __name__ == "__main__":
    print(calc(4)) 
    # -- OR --
    a,c = calc(4)
    print('area : ',a,'circumference: ',round(c,4)) 
    # round() helps to print how many digit you want in decimal i.e. precision

    print(calc())       # output - (0.0, 0.0)