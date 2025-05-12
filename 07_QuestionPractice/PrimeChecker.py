def check(num):
    isPrime = True
    for i in range(2,int(num/2)+1,1):
        if num%i == 0:
            isPrime = False
            break
    
    return isPrime

if __name__ == '__main__':
    n = int(input("Enter the number : "))
    print(check(n))