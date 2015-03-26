import random
def Init_Game ():
		player_red_name = raw_input ("Enter Red Player's Name: ")
		player_yellow_name = raw_input ("Enter Yellow Player's Name: ")
		# dictionary players has keys of 0 and 1, where the value is a list with the color at index 0 and player name at index 1
		players = {}
		players [0] = ['R', player_red_name]
		players [1] = ['Y', player_yellow_name]
		# firstplayer = int(random.choice('01'))
		# # this finds the player name from dictionary players that corresnponds to either 0 or 1 which was randmomly chosen above.
		# # this looks for key for either 0 or 1, and looks in the list at that value, for the string in index 1 of that
		# print "Player %s goes first!" % (players[firstplayer][1])
		print "Red Player %s goes first!" % (player_red_name)
		return players
players = Init_Game()

def Create_Board ():
	board = {}
	for column in range (0,7):
		for row in range (0,6):
			board[row, column] = 0
	return board

board = Create_Board()
print "players: "
print players
# print "first player: "
# print firstplayer
print "----Board: "
print board

# Player moves by giving a row, column tuple
# can only move by giving a row, column designation that is blank and has an item in (row-1, column)
# when we get a move, check if:
# 	if move_tuple is currently assigned as blank
# 		if move_tuple (row-1, column) is not blank
# then, make value at move_tuple = color_of_player
# else
# 	this position has nothing below it, please pick a different move
# 	rawinput Move
# 	else
# 		this position is not blank, please pick a different move
# 		rawinput Move 
# add checks for valid row and column numbers

def check_move (move_tuple, player, players):
		if board[move_tuple] == 0 :
			if move_tuple[1] != 0:
				if board[move_tuple[0], move_tuple[1]-1] != 0:
					check_move = True
					board[move_tuple] = players[player][0]
					print "board value at move tuple = %r" %  board[move_tuple]
				else:
					return False, "illegal move: there is no piece below this position!"
			else:
				board[move_tuple] = players[player][0]
				return True, "Yes!"
		else: 
			return False, "illegal move: there is already a piece in this position! please"

# this function checks if the move that the player chooses results in a win
# in this game, you win if your move leads to a four in a row along four dimensions: vertical, horizontal, w_diagonal, and e_diagonal
# vertical is easy, you just check the 3 spots below the move just made
#


# this is the main game loop that runs as long as win is not equal to True. It rotates through the two players, asks them for a move,
# checks if the move is valid, records the move, checks in there is a win, and then either runs through the loop again if there is no win,
# or, if there is a win, gracefully exits (or allows players to play again)

while True:
 	for player in players:
		print "----Board: "
		print board
		move_tuple_raw = raw_input ("Player %s enter your move. Remember to enter the column# first, followed by a comma, and then with the row#: " % (players[player][1]))
		move_tuple_list = move_tuple_raw.split(",")
		move_tuple = (int(move_tuple_list[0]),int(move_tuple_list[1]))
		print "move_tuple = %r" % (move_tuple,)
		if check_move(move_tuple, player, players)[0] == True:
			if check_win (move_tuple, player) == True:
				winner = player
				print "%s wins!" % (winner)
				play_again = raw_input ("Play again? [y/n]")
				if play_again == 'n':
					print "thanks!"
					break
				else:
					play_again == raw_input ("I don't understand you, play again? [y/n]")
			else:
				print 'next turn/n'
		else:
			print "%s" % check_move(move_tuple, player, players)[1]
		
	