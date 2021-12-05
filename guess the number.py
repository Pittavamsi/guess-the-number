import random

range = input("Type a number: ")

if range.isdigit():
    range = int(range)

    if range <= 0:
        print('Please type a number larger number')
        quit()
else:
    print('Please type a number')
    quit()

random_number = random.randint(0, range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("your number is more than that number!")
    else:
        print("Your number is less than that number!")

print("You guess is correct", guesses, "guesses")