from random import randint
print("-----------------------------------------")
print("Welcome to ALPHA Guessing Game, Have fun!")
print("------------------------------------------")
random_num = randint(1, 10)

while True:
	player_guess = int(input("Guess a number from 1 to 10: "))

	if player_guess < random_num:
		print("Too low!")
	elif player_guess > random_num:
		print("Too high!")
	else:
		print("You won!")
		continue_game = (input("Do you want to continue, (y/n)? ")).lower()
		
		if continue_game == "y":
			random_num = randint(1, 10)
			player_guess = None
		else:
			print("Thanks for guessing!")
			break
