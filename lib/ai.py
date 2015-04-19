# ==============================================================================
# TwitchPlaysCheckers
# HackRU Spring 2015 -- 4/18/2015
#
# ai algorithm to play checkers
# ==============================================================================
import copy
from random import choice

def simpleMove(id, board):
	for i in range(len(board)):
		for j in range(len(board)):
			if (board[i][j] and board[i][j].getOwner() == id):
				moves = set()
				__possibleJumps(board, id, i, j, 0, moves)
				if (not len(moves)): continue
				high = 0
				high_moves = []
				for m in moves:
					if m[2] > high:
						high = m[2]
						high_moves = [((i,j),(m[0],m[1]))]
					elif m[2] == high:
						high_moves.append(((i,j),(m[0],m[1])))
	return choice(high_moves)

def __possibleJumps(board, id, x, y, j, moves):
	size = len(board)
	puck = board[x][y]
	jumps = copy.deepcopy(j)
	boardcp = copy.deepcopy(board)
	# bounds check
	if (x > size or y > size or x < 0 or y < 0): return
	# check one direction
	if ((id == 'A' or (id == 'B' and puck.isKing())) and
		(x+1 < size and y+1 < size)):
		# jump down and right
		if (x+2 < size and y+2 < size and board[x+1][y+1] and
			board[x+1][y+1].getOwner() != id and not board[x+2][y+2] and
			not (x+2, y+2) in moves):
			boardcp[x][y] = None
			boardcp[x+1][y+1] = None
			boardcp[x+2][y+2] = puck
			moves.add( (x+2, y+2, jumps+1) )
			__possibleJumps(boardcp, id, x+2, y+2, jumps+1, moves)
		# jump down and left
		elif (x+2 < size and y-2 >= 0 and board[x+1][y-1] and
			board[x+1][y-1].getOwner() != id and not board[x+2][y-2] and
			not (x+2, y-2) in moves):
			boardcp[x][y] = None
			boardcp[x+1][y-1] = None
			boardcp[x+2][y-2] = puck
			moves.add( (x+2, y-2, jumps+1) )
			__possibleJumps(boardcp, id, x+2, y-2, jumps+1, moves)
	# check the other direction
	if ((id == 'B' or (id == 'A' and puck.isKing())) and
		x-1 >= 0 and y-1 >= 0):
		if (x-2 >= 0 and y+2 < size and board[x-1][y+1] and
			board[x-1][y+1].getOwner() != id and not board[x-2][y+2] and
			not (x-2, y+2) in moves):
			boardcp[x][y] = None
			boardcp[x-1][y+1] = None
			boardcp[x-2][y+2] = puck
			moves.add( (x-2, y+2, jumps+1) )
			__possibleJumps(boardcp, id, x-2, y+2, jumps+1, moves)
		elif (x-2 >= 0 and y-2 >= 0 and board[x-1][y-1] and
			board[x-1][y-1].getOwner() != id and not board[x-2][y-2] and
			not (x-2, y+2) in moves):
			boardcp[x][y] = None
			boardcp[x-1][y-1] = None
			boardcp[x-2][y-2] = puck
			moves.add( (x-2, y+2, jumps+1) )
			__possibleJumps(boardcp, id, x-2, y+2, jumps+1, moves)

# ------------------------------------------------------------------------------
if (__name__ == '__main__'):

	from checkers import CheckersManager

	game = CheckersManager()

	game.printBoard()
	game.move('A', 2,0, 3,1)
	game.printBoard()
	game.move('A', 3,1, 4,2)
	game.printBoard()
	game.move('B', 5,1, 3,3)
	game.printBoard()
	game.move('B', 5,7, 4,6)

	simpleMove('A', game.getBoard())
