import math
import copy
from functools import reduce


arr = [0 for i in range(12)]

with open("input.txt", "r") as file:
  # iterate over every line in a file
  for line in file.read().strip().split("\n"):
    for i in range(12):
      if line[i] == '1':
        arr[i] += 1
      else:
        arr[i] -= 1

g = ""
e = ""

for i in range(12):
  if (arr[i] > 0):
    g += "1"
    e += "0"
  else:
    g += "0"
    e += "1"

print(int(g, 2) * int(e, 2))