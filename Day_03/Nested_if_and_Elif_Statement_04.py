print("Welcome to the rollercoaster")
height = int(input("what is your height in cm ?"))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("what is your age ?"))
    if age < 12:
        print("Please pa $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $ 12.")
else:
    print("Sorry, you have to grow taller before you can ride.")