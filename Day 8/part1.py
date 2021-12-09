import math
import copy
from functools import reduce



with open("input.txt", "r") as f:
  c = 0
  
  # iterate over every line in a file
  for l in f.read().split("\n"):
    a, b = l.split(" | ")
    b = b.split(" ")
    for x in b:
      if len(x) == 7 or len(x) == 4 or len(x) == 3 or len(x) == 2:
        c += 1

  print(c)

