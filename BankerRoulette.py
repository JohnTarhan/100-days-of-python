# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_of_people = len(names)
random_choise = random.randint(0, number_of_people -1)
person_who_will_pay = names[random_choise]
print(person_who_will_pay + " will pay for the meal today.")
