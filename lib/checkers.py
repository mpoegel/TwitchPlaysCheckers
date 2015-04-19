# ==============================================================================
# TwitchPlaysCheckers
# HackRU Spring 2015 -- 4/18/2015
#
# Checker Game Manager Wrapper Class
# ==============================================================================
import copy

BOARD_SIZE = 8

# Helper Game Piece aka Puck Class
class Puck(object):
	# Static ID Counter
	ID_COUNT = 0
	# CONSTRUCTOR
	def __init__(self, owner):
		self.__id = self.__class__.ID_COUNT
		self.__owner = owner
		self.__isKing = False
		self.__class__.ID_COUNT += 1
	# ACCESSORS
	def getId(self): return self.__id
	def getOwner(self): return self.__owner
	def isKing(self): return self.__isKing

	# MODIFIERS
	def kingMe(self):
		if (self.__state):
			self.__state = True
			return True
		else: return False

# checkers game manager
class CheckersManager(object):
	# CONSTRUCTORS
	def __init__(self):
		self.__board = []
		self.__score = {
			'A': 0,
			'B': 0
		}
		# initialize the pieces on the board
		for i in range(BOARD_SIZE):
			self.__board.append([])
			for j in range(BOARD_SIZE):
				if (i < BOARD_SIZE/2 - 1):
					if ((j % 2 == 0 and i % 2 == 0) or (j % 2 == 1 and i % 2 == 1)):
						self.__board[i].append(Puck('A'))
						self.__score['A'] += 1
					else: self.__board[i].append(None)
				elif (i < BOARD_SIZE/2 + 1):
					self.__board[i].append(None)
				else:
					if ((j % 2 == 0 and i % 2 == 0) or (j % 2 == 1 and i % 2 == 1)):
						self.__board[i].append(Puck('B'))
						self.__score['B'] += 1
					else: self.__board[i].append(None)
	# PRIVATE METHODS
	def __isValidMove(self, player, x, y, xp, yp, board):
		puck = board[x][y]
		boardcp = copy.deepcopy(board)
		# bounds check
		if (x > BOARD_SIZE or y > BOARD_SIZE or x < 0 or y < 0 or
			self.__board[xp][yp]):
			return False
		# check one direction
		if ((player == 'A' or (player == 'B' and puck.isKing())) and
			(x+1 < BOARD_SIZE and y+1 < BOARD_SIZE)):
			# jump down and right
			if (x+2 < BOARD_SIZE and y+2 < BOARD_SIZE and
				board[x+1][y+1] and
				board[x+1][y+1].getOwner() != player and
				not board[x+2][y+2]):
				boardcp[x][y] = None
				self.__score[board[x+1][y+1].getOwner()] -= 1
				boardcp[x+1][y+1] = None
				boardcp[x+2][y+2] = puck
				if (xp == x+2 and yp == y+2):
					self.__board = copy.deepcopy(boardcp)
					return True
				else:
					return self.__isValidMove(player, x+2, y+2, xp, yp, boardcp)
			# jump down and left
			elif (x+2 < BOARD_SIZE and y-2 >= 0 and
				board[x+1][y-1] and
				board[x+1][y-1].getOwner() != player and
				not board[x+2][y-2]):
				boardcp[x][y] = None
				self.__score[board[x+1][y-1].getOwner()] -= 1
				boardcp[x+1][y-1] = None
				boardcp[x+2][y-2] = puck
				if (xp == x+2 and yp == y-2):
					self.__board = copy.deepcopy(boardcp)
					return True
				else:
					return self.__isValidMove(player, x+2, y-2, xp, yp, boardcp)
		# check the other direction
		if ((player == 'B' or (player == 'A' and puck.isKing())) and
			x-1 >= 0 and y-1 >= 0):
			if (x-2 >= 0 and y+2 < BOARD_SIZE and
				board[x-1][y+1] and
				board[x-1][y+1].getOwner() != player and
				not board[x-2][y+2]):
				boardcp[x][y] = None
				self.__score[board[x-1][y+1].getOwner()] -= 1
				boardcp[x-1][y+1] = None
				boardcp[x-2][y+2] = puck
				if (xp == x-2 and yp == y+2):
					self.__board = copy.deepcopy(boardcp)
					return True
				else:
					return self.__isValidMove(player, x-2, y+2, xp, yp, boardcp)
			elif (x-2 >= 0 and y-2 >= 0 and
				board[x-1][y-1] and
				board[x-1][y-1].getOwner() != player and
				not board[x-2][y-2]):
				boardcp[x][y] = None
				self.__score[board[x-1][y-1].getOwner()] -= 1
				boardcp[x-1][y-1] = None
				boardcp[x-2][y-2] = puck
				if (xp == x-2 and yp == y-2):
					self.__board = copy.deepcopy(boardcp)
					return True
				else:
					return self.__isValidMove(player, x-2, y-2, xp, yp, boardcp)
	# ACCESSORS
	def getBoard(self): return self.__board
	def printBoard(self):
		print('-' * (BOARD_SIZE*2 + 3))
		for i in range(BOARD_SIZE):
			print('| ', end='')
			for j in range(BOARD_SIZE):
				if (not self.__board[i][j]):
					print('. ', end='')
				elif (self.__board[i][j].isKing()):
					print(self.__board[i][j].getOwner(), end=' ')
				else:
					print(self.__board[i][j].getOwner().lower(), end=' ')
			print('|')
		print('-' * (BOARD_SIZE*2 + 3))
	# MODIFIERS
	def move(self, player, x, y, xp, yp):
		puck = self.__board[x][y]
		if (not puck):
			print("ERROR: No puck found at (" + str(x) +"," + str(y) + ")")
			return False
		if (x > BOARD_SIZE or y > BOARD_SIZE or x < 0 or y < 0):
			print("ERROR: (" + str(x) +"," + str(y) + ") is out of range of the board")
			return False
		if (xp > BOARD_SIZE or yp > BOARD_SIZE or xp < 0 or yp < 0):
			print("ERROR: (" + str(xp) + "," + str(yp) + ") is out of range of the board")
			return False
		if (puck.getOwner() != player.upper()):
			print("ERROR: Player " + player + " does have control of puck at (" + str(x) + "," + str(y) +")")
			return False
		if (self.__board[xp][yp]):
			print("ERROR: (" + str(x) + "," + str(y) + ") to (" + str(xp) + "," + str(yp) + ") is not a valid move")
			return False
		if (player == 'A' or (player == 'B' and puck.isKing())):
			if (xp == x+1 and yp == y+1 and not self.__board[xp][yp]):
				self.__board[x][y] = None
				self.__board[xp][yp] = puck
				if ((player == 'A' and xp == BOARD_SIZE-1) or
					(player == 'B' and xp == 0)):
					self__board[xp][yp].kingMe()
				return True
			elif (xp == x+1 and yp == y-1 and not self.__board[xp][yp]):
				self.__board[x][y] = None
				self.__board[xp][yp] = puck
				if ((player == 'A' and xp == BOARD_SIZE-1) or
					(player == 'B' and xp == 0)):
					self__board[xp][yp].kingMe()
				return True
		elif (player == 'B' or (player == 'A' and puck.isKing())):
			if (xp == x-1 and yp == y+1 and not self.__board[xp][yp]):
				self.__board[x][y] = None
				self.__board[xp][yp] = puck
				if ((player == 'A' and xp == BOARD_SIZE-1) or
					(player == 'B' and xp == 0)):
					self__board[xp][yp].kingMe()
				return True
			elif (xp == x-1 and yp == y-1 and not self.__board[xp][yp]):
				self.__board[x][y] = None
				self.__board[xp][yp] = puck
				if ((player == 'A' and xp == BOARD_SIZE-1) or
					(player == 'B' and xp == 0)):
					self__board[xp][yp].kingMe()
				return True
		if (self.__isValidMove(player, x, y, xp, yp, copy.deepcopy(self.__board))):
			self.__board[x][y] = None
			self.__board[xp][yp] = puck
			if ((player == 'A' and xp == BOARD_SIZE-1) or
				(player == 'B' and xp == 0)):
				self__board[xp][yp].kingMe()
			return True

		print("Move failed")
		return False

# ------------------------------------------------------------------------------
if (__name__ == '__main__'):

	game = CheckersManager()

	game.printBoard()
	game.move('A', 2,0, 3,1)
	game.printBoard()
	game.move('A', 3,1, 4,2)
	game.printBoard()
	game.move('B', 5,1, 3,3)
	game.printBoard()
	game.move('B', 5,7, 4,6)
	game.printBoard()
	game.move('B', 6,6, 5,7)
	game.printBoard()
	game.move('A', 2,2, 6,6)
	game.printBoard()
