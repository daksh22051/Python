# 14. Write a Python program to input the marks of four subjects (out of 100)
# and calculate the average and determine the grade as follows:
# Average >= 90: Grade A
# Average >= 80: Grade B
# Average >= 70: Grade C
# Average >= 60: Grade D
# Average >= 50: Grade E
# Average < 50: Grade F

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))

average = (sub1 + sub2 + sub3 + sub4) / 4

print("Average =", average)

if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print("Grade C")
elif average >= 60:
    print("Grade D")
elif average >= 50:
    print("Grade E")
else:
    print("Grade F")