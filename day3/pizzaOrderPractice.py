print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N")

# TODO: work out how much they need o pay based on ther size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs")

# TODO: work out how much to add to their bill based on their pepperoni choice.

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# TODO: work out their final amount basedon whether if they want extra cheese.

if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is: ${bill}.")