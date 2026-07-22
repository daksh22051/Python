# 13. Write a Python program to swap the first and last digits of a
# number using a while loop.

num = int(input("enter num:"))
last_digit = num % 10


while(num>9):
    num = num // 10
first_digit =num

print("first digit before swap =",first_digit)
print("last digit before swap=",last_digit)

temp = first_digit
first_digit = last_digit
last_digit = temp

print("first digit after swap =",first_digit)
print("last digit after swap=",last_digit)
