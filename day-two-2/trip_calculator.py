print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? "))
people_count = float(input("How many people to split the bill? "))

split_bill = (total_bill / people_count) * (1 + tip_percent / 100)
final_bill = "{:.2f}".format(split_bill)
print(f"Each person should pay: ${final_bill}")
