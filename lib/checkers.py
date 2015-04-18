# ==============================================================================
#
#
# ==============================================================================
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
		# initialize the pieces on the board
		for i in range(BOARD_SIZE):
			self.__board.append([])
			for j in range(BOARD_SIZE):
				if (i < BOARD_SIZE/2 - 1):
					if ((j % 2 == 0 and i % 2 == 0) or (j % 2 == 1 and i % 2 == 1)):
						self.__board[i].append(Puck('A'))
					else: self.__board[i].append(None)
				elif (i < BOARD_SIZE/2 + 1):
					self.__board[i].append(None)
				else:
					if ((j % 2 == 0 and i % 2 == 0) or (j % 2 == 1 and i % 2 == 1)):
						self.__board[i].append(Puck('B'))
					else: self.__board[i].append(None)
	# ACCESSORS
	def getBoard(self): return self.__board
	def printBoard(self):
		print('-' * (BOARD_SIZE*2 + 3))
		for i in range(BOARD_SIZE):
			print('| ', end='')
			for j in range(BOARD_SIZE):
				if (not self.__board[i][j]):
					print('x ', end='')
				elif (self.__board[i][j].isKing()):
					print(self.__board[i][j].getOwner(), end=' ')
				else:
					print(self.__board[i][j].getOwner().lower(), end=' ')
			print('|')
		print('-' * (BOARD_SIZE*2 + 3))
	# MODIFIERS
	

# ------------------------------------------------------------------------------
if (__name__ == '__main__'):

	game = CheckersManager()

	game.printBoard()
