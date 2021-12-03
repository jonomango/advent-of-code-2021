import math
import copy
from functools import reduce


x = 0
y = 0

with open("input.txt", "r") as file:
  # iterate over every line in a file
  for line in file.read().strip().split("\n"):
    s, n = line.split(" ")
    if s == "forward":
      x += int(n)
    elif s == "down":
      y += int(n)
    elif s == "up":
      y -= int(n)

print(x * y)
