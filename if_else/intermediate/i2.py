# 2. BMI Calculator:->Write a program that calculates BMI based on user
# input for weight (in kg) and height (in meters). Classify the BMI as
# "Underweight," "Normal," "Overweight," or "Obese" using if-else
# statements.

weight = float(input("enter your weight(in kg):"))
height = float(input("enter your height(in feet):"))

BMI = weight / (height*height)
if(BMI<18.5):
    print("underweight")
elif(BMI>=18.5 and BMI<=24.9):
    print("Normal")
elif(BMI>=25 and BMI<=29.9):
    print("overweight")
else:
    print("obese")