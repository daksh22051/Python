# 15. Write a Python program to calculate the product of the digits of
# a number using a while loop.


num = int(input("enter num:"))
mul = 1

while(num>0):
    temp = num % 10
    mul = mul * temp
    num = num //10
print("mul = ",mul)

