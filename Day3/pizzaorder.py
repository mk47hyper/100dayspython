print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
add_peperoni = input("Do you want peperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

bill = 0

if size == "S".lower():
    bill += 15
elif size == "M".lower():
    bill += 20
elif size == "L".lower():
    bill += 25
else:
    bill += 25

if add_peperoni == "Y".lower():
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y".lower():
    bill += 1

print(f"You final bill is : ${bill}")
