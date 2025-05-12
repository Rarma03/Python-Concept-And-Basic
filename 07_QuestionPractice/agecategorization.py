# while using input classify what type of data you are taking, else it will store in string format
userage = int(input("Enter Your Age : "))

if(userage>18):
    print("Adult")
elif(userage==18):
    print("Just At The Age")
else:
    print("Child")