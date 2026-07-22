# 18. Write a Python program to find the frequency of each digit in a
# given integer using a while loop.

num = int(input("enter num:"))
for i in range(10):
    temp = num
    count = 0
    while(temp>0):
        digit = temp % 10
        if(digit==i):
            count+=1
        temp = temp //10
    if(count>0):
        print(i , "*" ,count)
        