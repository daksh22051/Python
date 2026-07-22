# 6. Write a Python program to find the sum of all natural numbers
# between 1 to n using a while loop.


num = int(input("enter num:"))
i = 1
sum =0
while(i<=num):
    sum = sum + i
    i+=1
print("sum = ",sum)
