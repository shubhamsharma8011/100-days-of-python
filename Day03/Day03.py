#Control flow and Logical Operators

#Check whether a number is odd or even
num=int(input("Enter a number: "))
if num%2==0:
    print("It is Even number")
else:
    print("It is Odd number")

#Nested-If
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi=weight/height**2
if bmi<18.5:
    print("Underweight")
elif 18.5<bmi and bmi<25:
    print("Normal weight")
elif bmi>=25:
    print("Overweight")


