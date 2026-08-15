#Who will pay the bill?

a=input("Enter the name of first member: \n")
b=input("Enter the name of second member: \n")
c=input("Enter the name of third member: \n")
d=input("Enter the name of fourth member: \n")
members=[a,b,c,d]

import random
bill_payer=random.choice(members)
print(f"Bill will be paid by {bill_payer}")