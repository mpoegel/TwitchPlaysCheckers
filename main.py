# ==============================================================================
# TwitchPlaysCheckers
# HackRU Spring 2015 -- 4/18/2015
#
# main file
# ==============================================================================
import sys
import random
import time
sys.path.append('lib')

from checkers import CheckersManager
from player import Player
from twitch_chat_reader import TwitchChatReader
# from make_board import drawBoard
import ai


def main():

	Game = CheckersManager()
	Chat = TwitchChatReader()
	ai_score = 0
	ai_ID = 'A'
	twitch_score = 0
	twitch_ID = 'B'

	while not Game.isOver():
		move = ai.simpleMove(ai_ID, Game.getBoard())
		Game.move(ai_ID, move[0][0], move[0][1], move[1][0], move[1][1])
		Game.printBoard()
		if (Game.isOver()): break
		move = Chat.read_chat()
		while not Game.move(twitch_ID, move[0][0]-1, move[0][1]-1, move[1][0]-1, move[1][1]-1):
			move = Chat.read_chat()
		Game.printBoard()

# ------------------------------------------------------------------------------
if (__name__ == '__main__'):

	random.seed(time.time())
	main()
