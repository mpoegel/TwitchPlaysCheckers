import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as m
#adds point to board
def add_piece(x_,y_, board, piece):
    if piece == None:
        return board
    rgb = np.asarray([piece[:,:,0], piece[:,:,1], piece[:,:,2]])
    mask = (rgb[0] != 255) & (rgb[1] != 255) & (rgb[2] != 255)

    x = board.shape[0]/8
    y = board.shape[1]/8
    x_start = x*x_
    y_start = y*y_
    for i in range(x_start, x_start +x):
        for j in range(y_start, y_start+y):
            if mask[i-x_start,j-y_start]:
                board[i, j] = piece[i-x_start, j-y_start]
    return board

def drawBoard(board):
	#Reads in images
	board = cv2.imread("images/board.jpg")
	red = cv2.imread("images/red.png")
	black = cv2.imread("images/black.png")
	red_king = cv2.imread("images/red_king.png")
	black_king = cv2.imread("images/black_king.png")
	
	#sets counters to iterate through board
	x = 0
	y = 0
	none = 0
	#Looping through given board state and makes board
	for row in board:
		y = 0
		for piece in row:
			if piece == None:
				none  = 0
			elif piece == "a":
				board = add_piece(x,y, board, red)
			elif piece == "A":
				board = add_piece(x,y, board, red_king)
			elif piece == "b":
				board = add_piece(x,y, board, black)
			elif piece == "B":
				board = add_piece(x,y, board, black_king)
			#Unexpected input from board input
			else:
				print "Invalid input"
			y+=1
		x+=1
		
	sigma = 2
	ksize = (2*sigma+1,2*sigma+1)
	board = cv2.GaussianBlur(board, ksize, sigma)
	cv2.imwrite("images/current.png", board)
