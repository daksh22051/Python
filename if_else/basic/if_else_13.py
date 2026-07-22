# 13. Write a Python program to input the month number (1 for January, 2 for
# February, etc.) and print the number of days in that month (considering
# leap years)

month = int(input("enter month num:"))
year = int(input("enter year:"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    leap = True;
else:
    leap = False

if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("31 days")
elif(month==2):
    if(leap==True):
        print("it has 29 days")
    else:
        print("it has 28 days")
else:
    print("it haas 30 month")