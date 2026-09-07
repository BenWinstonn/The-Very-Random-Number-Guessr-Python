import random

print("===================================")
print("The Very Random Number Guessr Game")
print("===================================")

random_number = random.randint(1, 100)
guesses = 0

while True:
    try:
        player_guess = int(input("\nPlease guess a number from 1-100: "))
        guesses += 1 

        if 1 <= player_guess <= 100:
            if player_guess > random_number:
                print("Too High!")
            elif player_guess < random_number:
                print("Too Low!")
            elif player_guess == random_number:
                print(f"Congratulations! You guessed it in {guesses} tries! It's {random_number}")

                player_try_again = input("\nWould you want to play again? (y/n): ").lower()
                
                if player_try_again in ["y", "yes"]:
                    random_number = random.randint(1, 100)
                    guesses = 0 
                    continue
                elif player_try_again in ["n", "no"]:
                    print("Good Bye!")
                    break
                else:
                    print("Not a valid answer. Quitting game.")
                    break
                    
        else:
            print("Please guess from 1-100")

    except ValueError:
        print("Not a Valid Number.")
