#Import Random
import random

#random.randint
random_int=random.randint(1,6)
print(random_int)

#random.random
random_0to100=random.random()*100
print(random_0to100)

#random.float
random_float=random.uniform(1,10)
print(random_float)
print()


#Lists
alphabets=["a","e","i","o","j"]
alphabets[-1]="u"
alphabets.append("k")
alphabets.extend(["l","m"])
print(alphabets)


