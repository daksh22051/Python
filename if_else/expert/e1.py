# Airline Reservation System:-> Implement an airline reservation
# system. Ask the user for their destination and the class of service
# (Economy, Business, First). Based on the input, display the ticket price.
# Consider different pricing for different destinations and classes.

destination = input("enter your destination(Delhi,Mumbai,Goa):").lower()
ser = input("enter your class or service(Economy, Business, First):")

if(destination=='delhi'):
    if(ser=='Economy'):
        print("you ticket price is: $100")
    elif(ser=='Bussines'):
        print("your ticket price is: $150")
    else:
        print("you ticket price is: $200")

elif(destination=='mumbai'):
    if(ser=='Economy'):
     print("you ticket price is: $150")
    elif(ser=='Bussines'):
        print("your ticket price is: $200")
    else:
        print("you ticket price is: $250")

else:
    if(ser=='Economy'):
            print("you ticket price is: $250")
    elif(ser=='Bussines'):
            print("your ticket price is: $300")
    else:
            print("you ticket price is: $350")