print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <=12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
        
        wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
else: 
    print("Sorry you have to grow taller before you can ride")