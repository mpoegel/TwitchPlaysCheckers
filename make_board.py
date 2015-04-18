import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as m

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



board = cv2.imread("images/board.jpg")
board = cv2.cvtColor(board, cv2.COLOR_BGR2RGB)
red = cv2.imread("images/red.png")
red = cv2.cvtColor(red, cv2.COLOR_BGR2RGB)

black = cv2.imread("images/black.png")
red_king = cv2.imread("images/red_king.png")
black_king = cv2.imread("images/black_king.png")
red_king = cv2.cvtColor(red_king, cv2.COLOR_BGR2RGB)
black_king = cv2.cvtColor(black_king, cv2.COLOR_BGR2RGB)
x = 0
y = 0
setup = [[None, red, None, red, None, red, None, red],
[red, None,red, None,red_king, None,red, None],
[None, red, None, red, None, red, None, red],
[None, None,None,None,None,None,None,None],[None, None,None,None,None,None,None,None],
[None, black, None, black_king, None, black, None, black],
[black, None,black, None,black, None,black, None],
[None, black, None, black, None, black, None, black]]
for row in setup:
    y = 0
    for piece in row:
        board = add_piece(x,y, board, piece)
        y+=1
    x+=1
sigma = 2
ksize = (2*sigma+1,2*sigma+1)
board = cv2.GaussianBlur(board, ksize, sigma)

plt.imshow(board)
plt.axis("off")
plt.show()
