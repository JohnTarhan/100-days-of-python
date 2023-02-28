# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

trueCount = 0
loveCount = 0

trueCount += name1.count('t') + name2.count('t')
trueCount += name1.count('r') + name2.count('r')
trueCount += name1.count('u') + name2.count('u')
trueCount += name1.count('e') + name2.count('e')

loveCount += name1.count('l') + name2.count('l')
loveCount += name1.count('o') + name2.count('o')
loveCount += name1.count('v') + name2.count('v')
loveCount += name1.count('e') + name2.count('e')

scoreStr = str(trueCount) + str(loveCount)
score = int(scoreStr)


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
