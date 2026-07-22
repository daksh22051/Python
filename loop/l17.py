# 17. Write a Python program to check whether a number is a
# palindrome or not using a while loop.


num = int(input("enter num:"))
rev =0
dup = num
while(num>0):
    temp = num % 10
    rev = (rev*10) + temp
    num = num // 10
print("rev number = ",rev)
num = dup
if(num==rev):
    print("pallindrome number")
else:
    
    print("not a pallindrome number")