import math
import copy
from functools import reduce

def s(b, x, y):
  a = []
  if x > 0:
    a.append(b[y][x-1])
  if y > 0:
    a.append(b[y-1][x])
  if x < len(b[y])-1:
    a.append(b[y][x+1])
  if y < len(b)-1:
    a.append(b[y+1][x])
  return a

with open("input.txt", "r") as f:
  b = []
  # iterate over every line in a file
  for l in f.read().split("\n"):
    b.append(l)

  c = 0
  for y in range(len(b)):
    for x in range(len(b[y])):
      #print(s(b, x, y))
      if all(int(b[y][x]) < int(i) for i in s(b, x, y)):
        c += int(b[y][x]) + 1
  print(c)
