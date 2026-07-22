# 9. Write a Python program to print the multiplication table of any
# number using a while loop.

num = int(input("enter num:"))
i = 1
while(i<=10):
    print(num , "*" ,i , "=" , num * i)
    i+=1
    