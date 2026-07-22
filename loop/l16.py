# 16. Write a Python program to enter a number and print its reverse
# using a while loop.
num = int(input("enter num:"))
rev =0
while(num>0):
    temp = num % 10
    rev = (rev*10) + temp
    num = num // 10
print("rev number = ",rev)