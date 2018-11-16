import random 
computer_ans = random.choice(('r', 'p', 's'))

num_turns = 5
User_score = 0
Computer_score = 0




print("Welcome to Rock Paper Scissors!")
ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")

while num_turns > 0:
	computer_ans = random.choice(('r', 'p', 's'))
	
	if ans == "r":
		if computer_ans == "p":
			print("Computer: " + computer_ans)
			print("Paper beats rock, the computer won this round!")
			Computer_score += 1
			num_turns -= 1
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")

		elif computer_ans == "s":
			print("Computer: " + computer_ans)
			print("Rock beats scissors, you won this round!")
			User_score += 1
			num_turns -= 1
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")
		
		else:
			print("It was a draw!")
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			num_turns -= 1
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")


	
	elif ans == "p":
		if computer_ans == "r":
			print("Computer: " + computer_ans)
			print("Paper beats rocks, you won this round!")
			User_score += 1
			num_turns -= 1
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")

		elif computer_ans == "s":
			print("Computer: " + computer_ans)
			print("Scissors beat paper, the computer won this round!")
			Computer_score += 1
			num_turns -= 1
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")

		else:
			print("It was a draw!")
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			num_turns -= 1
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")


	elif ans == "s":
		if computer_ans == "r":
			print("Computer: " + computer_ans)
			print("Rock beats scissors, the computer won this round!")
			Computer_score += 1
			num_turns -= 1
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")
		
	
		elif computer_ans == "p":
			print("Computer: " + computer_ans)
			print("Scissors beat paper, you won this round!")
			User_score += 1
			num_turns -= 1
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")

		else: 
			print("It was a draw!")
			print("User score: " + str(User_score))
			print("Computer score: " + str(Computer_score))
			num_turns -= 1
			print("Turns left: " + str(num_turns))
			print("-----------------")
			ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")
	
	else:
		print("Sorry, I didn't recognise your answer.")
		print("-----------------")
		ans = input("Choose 'r' for rock, 'p' for paper, 's' for scissors ")
		


print("You have run out of turns! The scores are: ")
print("User score: " + str(User_score))
print("Computer score: " + str(Computer_score))
if User_score > Computer_score:
	print("Congrats! You've won!")

elif Computer_score > User_score:
	print("The computer has won")

else:
	print("It was a draw!")