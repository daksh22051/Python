# Discount Calculator:->Develop a program that asks the user to enter
# the total amount of a purchase. If the amount is greater than $100,
# apply a 10% discount and print the final amount. Otherwise, print the
# original amount.

amount = int(input("enter total amount of a purchase:"))

if(amount>100):
    discount = amount * 0.10
    final_amount = amount - discount
    print("discount applied = $",discount)
    print("final amount to pay: $",final_amount)

else:
    print("discoun applied")
    print("final amount to pay: $",amount)