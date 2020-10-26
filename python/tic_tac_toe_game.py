##### Tic Tac Toe Game - Milestone Project 1 #####
##### Programmed By - Nik O'Brien - nikolas.j.obrien@gmail.com - 10/25/2020 #####

# This is the first milestone project for the Python Certification Course (2020 Complete Python Bootcamp: From Zero to Hero in Python) via Udemy #

# Ideally this file will contain all original code and my personal solution to the project #
# If I need to reference the course's solution I will indicate with the comment "REFERENCED SOLUTION" in the code #

# Purpose - The goal is to create a 2 player interactive tic tac toe game #

##################################################################################################################################################

# DEFINITION OF FUNCTIONS #
# this function displays the updated game board #
def display_game(input_1):
    # sets up a 3x3 board where each box is also multi-dimensional in order to make them numbered #
    row_1 = f'1    |2    |3    \n  {input_1[0]}  |  {input_1[1]}  |  {input_1[2]}   \n     |     |    \n_________________'
    row_2 = f'4    |5    |6    \n  {input_1[3]}  |  {input_1[4]}  |  {input_1[5]}   \n     |     |    \n_________________'
    row_3 = f'7    |8    |9    \n  {input_1[6]}  |  {input_1[7]}  |  {input_1[8]}   \n     |     |   '
    
    # print statement and the board #
    print('Here is the current board.')
    print(row_1)
    print(row_2)
    print(row_3)

# this function reads in the user input for a box to fill #
def user_choice(player):
	#initialize
	good_num = False

	# while loop to validate the input, make sure its digit and in range and its box is empty #
	while good_num == False:
 		user_input = input("Please enter the number (1-9) of the box you'd like to mark: ")

 		if user_input.isdigit() == False:
 			print("Input was not a digit.")
 		else:
 			if int(user_input) not in range(1,10):
 				print("Input was not a number in the valid range.")
 			elif input_1[int(user_input)-1] != ' ':
 				# added to account for not selecting already chosen boxes #
 				print("Box has already been filled. Please pick a different number.")
 			else:
 				user_input = int(user_input)
 				good_num = True

 	# populates the proper box with the sign depending on player #
	if player == 1:
		input_1[user_input-1] = 'X'
	else:
		input_1[user_input-1] = 'O'
	
	return(user_input)

 # this function appends the box of choice to the players list to check against winning lists #
def choice_add(player):
	# bring in the user input
 	user_input = user_choice(player = player)

 	# append to appropriate list accordingly #
 	if player == 1:
 		player_1_list.append(user_input)
 		player_1_list.sort()
 	else:
 		player_2_list.append(user_input)
 		player_2_list.sort()

# this function checks if there is a winner #
def check_winner(winning_list):
	# initialize #
	winner = 0

	# check each possible winning list against the player selections #
	# here, we are comparing sets #
	for j in winning_list:
		if set(j) <= set(player_1_list):
			winner = 1
			display_game(input_1)
			print('Player 1 Wins!')
			break
		elif set(j) <= set(player_2_list):
			display_game(input_1)
			winner = 2
			print('Player 2 Wins!')
			break

	# if no winner, winner still equals 0 #
	return(winner)

# this function asks if the players want to play again #
def player_again():
	# initialize #
	valid_play = False

	# validates that the input is y or n and then returns it to the program #
	while valid_play == False:
		playit = input("Would you like to play again - Y/N: ")

		if playit.lower() == 'y' or playit.lower() == 'n':
			valid_play = True
			return(playit)
		else:
			print('You did not enter a valid response.')



# START OF PROGRAM #
# initialize #
play_again = True

print("Hello! Welcome to Nik's Tic Tac Toe Game!\n\nPlayer 1 is 'X'\nPlayer 2 is 'O'\n")

# play as long as players want to keep playing #
while play_again == True:
	print("Let's do it!!!")

	# initialize  all boxes as blank and define the possible winning lists #
	input_1 = list(' '*9)
	winning_list = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

	# initialize empty player lists to append to #
	player_1_list = []
	player_2_list = []

	# start count so that once all boxes are filled and no winner, a draw is declared #
	count = 1

	# total of 9 turns until draw #
	for i in range(1,10):
		# add to count #
		count += 1

		# define player by even/oddness #
		if i%2 == 0:
			player = 2
		else:
			player = 1

		# display board before turn #
		display_game(input_1)

		# player makes choice #
		print(f'Player {player} make your choice.')
		choice_add(player = player)

		# checks for winner #
		winner = check_winner(winning_list)
		if winner == 1 or winner == 2:
			break
		else:
			if count > 9:
				print("It's a draw!")
				break
			else:
				continue

	# once game is over ask to play again, if 'n' break the while loop #
	playit = player_again()
	if playit.lower() == 'n':
		play_again = False