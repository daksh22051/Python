# 7. Write a Python program to find the sum of all even numbers between
# 1 to n using a while loop.

num = int(input("enter num:"))
i = 1
sum =0
while(i<=num):
    if(i%2==0):
        sum = sum + i
    i+=1
print("even sum = ",sum)
