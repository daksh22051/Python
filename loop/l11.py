# 11. Write a Python program to find the first and last digit of a
# number using a while loop.

num = int(input("enter num:"))
last_digit = num % 10


while(num>9):
    num = num // 10
first_digit =num
print("first digit =",first_digit)
print("last digit=",last_digit)
