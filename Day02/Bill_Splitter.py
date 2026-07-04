#Bill Splitter
print("Welcome to Splitting the bill Calculator!")
print()
bill=int(input("What is the total bill?\n"))
person=int(input("What is number of members present?\n"))
tip=int(input("How much percent of tip do you want to include?\n"))
bill_after_splitting=((bill)*(tip/100)+(bill))/person
print("Each of the member have to give: ", int(bill_after_splitting))

