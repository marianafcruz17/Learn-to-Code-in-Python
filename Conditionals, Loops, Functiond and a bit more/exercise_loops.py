import random
people = []

for x in range(0,8):
    person = input("Type the name of a person: ")
    people.append(person)

index = random.randint(0,7)

random_person = people[index]

print("Picking a random person: ",random_person)


colors = ["white","pink","black","red","blue","yellow","green","purple","gray"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I'm thinking about a color, can you guess it: ")

    while True:
        if color==guess:
           break
        else:
            guess = input("Nope. Try again: ")

    print("You guessed it! I was think about ", color)

    play_again = input("Let's play again? Type 'no' to quit ")

    if play_again.lower()=='no':
        break
print("It was fun, thanks for playing")
