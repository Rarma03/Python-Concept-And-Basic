n = int(input("Enter Num : "))

sum = 0
for val in range(n+1):
    sum += val if val%2==0 else 0

print(sum)