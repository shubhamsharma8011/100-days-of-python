fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print()

student_score=[20,30,45,60,78,89,34,23,45,51,65,84]
#Finding the sum of list
sum=0
for i in student_score:
    sum+=i
print(sum)

#Finding the largest number from the list
max=0
for i in student_score:
    if i>max:
        max=i
print(max)