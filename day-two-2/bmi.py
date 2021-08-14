height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2
bmi_to_int =int(bmi)
print("Your Body Mass Index is: \n" + str(bmi_to_int))