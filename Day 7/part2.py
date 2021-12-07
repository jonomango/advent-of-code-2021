import math
import copy
from functools import reduce

def calc(l, y):
  cost = 0
  for x in l:
    c = abs(x - y)
    # summation of i
    cost += c * (c + 1) / 2
  return cost

with open("input.txt", "r") as f:
  # iterate over every line in a file
  z = [int(x) for x in f.read().split(",")]

  mn = 9999999999999
  for x in range(min(z), max(z)):
    c = calc(z, x)
    if c < mn:
      mn = c
  print(mn)



