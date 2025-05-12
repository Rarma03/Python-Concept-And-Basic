passw = input("Enter Your password plis : ")

str = 0

num = ['0','1','2','3','4','5','6','7','8','9']
spc = ['@', '#', '$', '%', '^', '&', '*']

for val in num:
    if val in passw:
        str+=1
        break

for val in spc:
    if val in passw:
        str+=1
        break

for val in passw:
    if val.isupper():
        str+=1
        break

for val in passw:
    if val.islower():
        str+=1
        break

if len(passw) > 7:
    str+=1

print(f'Your Password strength is {str}/5')
print('THANK YOU FOR USING OUR SERVICE')