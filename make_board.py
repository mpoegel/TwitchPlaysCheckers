import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as m
def add_piece(x_,y_, board, piece):
    white = [255,255,255]
    rgb = np.asarray([piece[:,:,0], piece[:,:,1], piece[:,:,2]])
    mask = (rgb[0] < 230) & (rgb[1] < 230) & (rgb[2] < 230)

    x = board.shape[0]/8
    y = board.shape[1]/8
    x_start = x*x_
    y_start = y*y_
    for i in range(x_start, x_start +x):
        for j in range(y_start, y_start+y):
            if mask[i-x_start,j-y_start]:
                board[i, j] = piece[i-x_start, j-y_start]
    return board



board = cv2.imread("images/board.jpg")
board = cv2.cvtColor(board, cv2.COLOR_BGR2RGB)
red = cv2.imread("images/red.jpg")
red = cv2.cvtColor(red, cv2.COLOR_BGR2RGB)
x = board.shape[0]/8
y = board.shape[1]/8



black = cv2.imread("images/black.jpg")
for i in range(8):
    for j in range(8):
        board = add_piece(i,j, board, red)
sigma = 1
ksize = (2*sigma+1,2*sigma+1)
board = cv2.GaussianBlur(board, ksize, sigma)
plt.imshow(board)
plt.axis("off")
plt.show()
