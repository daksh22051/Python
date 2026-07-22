# Create a program for a movie ticket booking system. Ask the user for
# their age and determine the ticket price accordingly:
# Children (age < 12): $5
# Adults (12 <= age < 18): $10
# Adults (age >= 18): $15
age = int(input("enter you age:"))
if(age<12):
    print("ticket price : $5")
elif(age>=12 and age<18):
    print("ticket price: $10")
elif(age>=18):
    print("ticlet price: $15")