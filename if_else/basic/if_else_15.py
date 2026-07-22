# 15. Write a Python program to input the price of an item and the money
# given by the customer, then calculate and print the change to be returned.

price = float(input("Enter the price of the item: "))
money = float(input("Enter the money given by the customer: "))

if money < price:
    print("Insufficient money.")
else:
    change = money - price
    print("Change to be returned =", change)    