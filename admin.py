print('Enter your username')
userid=input()
if userid=='Admin':     #outerif
    print('Enter the password')
    p=int(input())
    if p==123:              #inner if
        print("Login success")
    else:
        print("Incorrect password")

else:
    print("Incorrect username")
