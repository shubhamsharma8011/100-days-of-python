print("Welcome to Treasure Island. Your mission is to find the treasure.")
first_step=input("Left or Right?\n")
if first_step=="Left":
    second_step=input("Swim or Wait?\n")        
    if second_step=="Wait":
        third_step=input(("Which door? Red, Blue or Yellow\n"))
        if third_step=="Red":
            print("Burned by fire.\nGame Over.")
        elif third_step=="Blue":
            print("Eaten by beasts.\nGame Over.")
        elif third_step=="Yellow":
            print("You Win")
        else:
            print("Wrong Input")
    else:
        print("Attacked by trout\nGame Over")
else:
    print("Fell into an home.\nGame Over")