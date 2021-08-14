print(round(8.6666666666, 2))
print(type(round(8.6666666666, 2)))
# floor division
print(8 // 3)
print(type(8 // 3))

result = 4 / 2
result /= 2
print(result)

score = 0
# User scores a point
score += 8
score -= 2
score *= 2
score /= 4

print(score)

# Throws error str + int
# print("Your score is " + score)

score = 0
height = 1.8
isWinning = True
# f-String
print(
    f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
