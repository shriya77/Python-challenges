radius = float(input("Enter circle's radius in cm: "))
pi = 3.14
unit1 = "cm"
unit2 = "cm^2"

user_input = input("Enter 'a' to find area and 'c' to find circumference: ")
if user_input == "a":
    print(pi*(radius)**2, unit2)
else:
    print(2*pi*radius, unit1)
