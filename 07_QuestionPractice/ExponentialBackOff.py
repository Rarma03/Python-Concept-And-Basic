import time

initial_wait_time = 1
max_retry = 5
attempt = 0

while attempt<max_retry:
    userpass = input("Enter Password : ")
    if userpass == 'abc123':
        print("Login")
        exit()
    
    print('attempt number : ', attempt+1,'please wait for : ', initial_wait_time)

    time.sleep(initial_wait_time)
    
    initial_wait_time *= 2
    attempt+=1

print("System is Locked")