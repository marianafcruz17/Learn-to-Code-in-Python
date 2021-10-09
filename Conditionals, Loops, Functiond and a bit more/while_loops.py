x = 0
people = []

while x<5:
    person = input("Type the name of a person: ")
    people.append(person)
    x += 1

print(people)

import random

number = random.randint(0,10)

guess = int(input("I'm thinking about a number. Can you guess it? "))

while True:
    if guess==number:
        break
    else:
        guess = int(input("Nope. Try again: "))
        
print("You guessed it. I was think about",number)
