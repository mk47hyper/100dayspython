from itertools import count

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combinedstring = name1 + name2

t = combinedstring.count("t")
r = combinedstring.count("r")
u = combinedstring.count("u")
e = combinedstring.count("e")

true = t + r + u + e

l = combinedstring.count("l")
o = combinedstring.count("o")
v = combinedstring.count("v")
e = combinedstring.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
