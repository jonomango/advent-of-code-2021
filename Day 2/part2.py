import math
import copy
from functools import reduce


aim = 0
depth = 0
pos = 0

with open("input.txt", "r") as file:
  # iterate over every line in a file
  for line in file.read().strip().split("\n"):
    s, n = line.split(" ")
    if s == "forward":
      pos += int(n)
      depth += int(n) * aim
    elif s == "down":
      aim += int(n)
    elif s == "up":
      aim -= int(n)

print(depth * pos)
