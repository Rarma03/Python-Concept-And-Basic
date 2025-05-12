# LEARN TO OPEN THE FILE 
f = open(r'D:\Python - Learning\08_Iteration_tools\readablefile.py')
#   -- OR --
f = open('D:\\Python - Learning\\08_Iteration_tools\\readablefile.py')


# LEARN TO READ FILE
a = f.readline()
print(a)
#   -- OR --
a = f.__next__()
print(a)

# notes
# 1. when we use readline or next then we permanently moves to next line, i.e. when you use loop below
#    the starting line will be 3rd

# 2. readline and next works same, the only difference is readline is more enhanced version of next and
#    handles exception greatly
#       e.g readline return "" when file ends, next returns error "stop iteration" when file ends


# LEARN TO READ MULTIPLE LINE IN ONE GO
for sentence in f:
    print(sentence)
print("-------------------------------")
#   -- OR --
f = open('D:\\Python - Learning\\08_Iteration_tools\\readablefile.py')  # reset the file line to 1st
while True:
    line = f.readline()
    if not line:
        break
    print(line, end = "") # set end to anything if you want