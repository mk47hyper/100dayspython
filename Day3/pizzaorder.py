print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_peperoni = input("Do you want peperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    bill += 25

if add_peperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"You final bill is : ${bill}")


# if size == "S":
#     bill += 15
#     if add_peperoni == "Y":
#         bill += 2
#         print(f"Small pizza coming right up.")
#         if size == "M":
#             bill = 20
#             if add_peperoni == "Y":
#                 bill += 3
#                 print(f"Medium pizza coming right up.")
#                 if size == "L":
#                     bill = 25
#                     if add_peperoni == "Y":
#                         bill += 3
#                         print(f"Large pizza coming right up.")
#                     else:
#                         print("Maybe next time.")
