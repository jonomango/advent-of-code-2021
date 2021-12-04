import math
import copy
from functools import reduce

order = []
boards = []

with open("input.txt", "r") as file:
  lines = file.read().strip().split("\n")

  order = lines[0].split(',')
  lines = lines[2:]

  board = []
  for line in lines:
    if len(line) == 0:
      boards.append(board)
      board = []
    else:
      board.append([x for x in line.strip().split(' ') if len(x) > 0])
  boards.append(board)

def iterate(board, num):
  for y in range(5):
    for x in range(5):
      if board[y][x] == num:
        board[y][x] = 'X'

def did_win(board):
  for y in range(5):
    if board[y][0] == 'X' and board[y][1] == 'X' and board[y][2] == 'X' and board[y][3] == 'X' and board[y][4] == 'X':
      return True
  
  for x in range(5):
    if board[0][x] == 'X' and board[1][x] == 'X' and board[2][x] == 'X' and board[3][x] == 'X' and board[4][x] == 'X':
      return True
  
  return False

def solve(boards):
  for o in order:
    losers = []

    for board in boards:
      iterate(board, o)

      if not did_win(board):
        losers.append(board)
      else:
        if len(boards) != 1:
          continue

        s = 0
        for x in range(5):
          for y in range(5):
            if board[y][x] != 'X':
              s += int(board[y][x])

        print(s * int(o))

    boards = copy.deepcopy(losers)

solve(boards)
