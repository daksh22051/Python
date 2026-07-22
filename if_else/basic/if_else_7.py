# 7. User Authentication: Create a program that asks the user to enter a
# username and password. If the username is "admin" and the password is
# "password123," print "Login successful." Otherwise, print "Invalid
# credentials."

username = input("enter username:")
password = input("enter password:")
if((username=='admin' and password=='password123')):
    print("Login Successful")
elif((username.strip()=="" or password.strip()=="")):
    print("please enter username and password")
else:
    print("invalid credentials")

