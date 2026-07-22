# 14. Write a Python program to calculate the sum of the digits of a
# number using a while loop.

num = int(input("enter num:"))
sum = 0

while(num>0):
    temp = num % 10
    sum = sum + temp
    num = num //10
print("sum = ",sum)

