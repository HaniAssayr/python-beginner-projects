import random

secret_number = random.randint(1, 100)
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("Enter your guess number:"))
    guess_count += 1

    if guess == secret_number:
        print("you won!")
        print(f"you won it in {guess_count} attempts")
    elif guess < secret_number:
        print(" too low")
    else:
        print("too high")

else:
    print("game is over!")