# 8. Write a Python program to check if a given year is a leap year or not.

year= int(input("enter num:"))
if((year % 400==0) or (year%4==0 and year %100!=0)):
    print("leap year");
else:
    print("not a leap year");

