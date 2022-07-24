print("Welcome to the roller coaster!")
height = (int(input("What is your height in cm?\n")))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?\n"))

    if age < 12:
        print("Please pay $5.")
        bill = 5
    elif age <= 18:
        print("Please pay $7.")
        bill = 7
    else:
        print("Please pay $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y or N.\n")
    if wants_photo == "Y".lower():
        # Add 3$ to their bill
        bill += 3
    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
