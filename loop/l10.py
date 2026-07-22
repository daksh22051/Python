# 10. Write a Python program to count the number of digits in a
# given number using a while loop.

num = int(input("enter num:"))
count = 0
while(num>0):
    num = num // 10
    count+=1
print("count = ",count)

