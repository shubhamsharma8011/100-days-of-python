#String
print(type("1234"+"5678"))

#Integer
print(type(1234+5678))

#Large Integers ( underscore works as comma)
print(type(12_321_567))

#Float
print(type(12.3+12.6))

#Boolean
print(type(True))
print(type(False))

#Type Casting
num=12.0
print(type(num))
num2=int(num)
print(type(num2))
print()

#Type Error and Conversion
name=input("Enter your name: ")
length=len(name)
print("Number of letters in your name: " + str(length))
print()

#Arithmetic Operators
print(7+3)
print(7-3)
print(7*3)
print(7**3)
print(7/3)
print(7//3)
print(7%3)
print()

#PEMDAS(Parentesis,Exponents,Mutiply/Division,Add/Subs) Left to right
print(3/3+3*3-3)
print()

#Calculate the BMI
height = 1.65 
weight = 84
bmi = weight/height**2
print(round(bmi,2))
print()

#f-string
age=12
grade=7
print(f"Your age is {age} and you are studying in grade {grade}")