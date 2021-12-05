import math
import copy
from functools import reduce

map = {}

with open("input.txt", "r") as f:
  # iterate over every line in a file
  for l in f.read().strip().split("\n"):
    l = [[int(y) for y in x.split(",")] for x in l.split(" -> ")]
    s, e = l[0], l[1]

    x = s[0]
    y = s[1]
    dx = e[0] - s[0]
    dy = e[1] - s[1]
    dx = 1 if dx > 0 else -1 if dx < 0 else 0
    dy = 1 if dy > 0 else -1 if dy < 0 else 0

    while x != e[0] or y != e[1]:
      if (x, y) not in map:
        map[(x, y)] = 0
      map[(x, y)] += 1

      x += dx
      y += dy

    if (x, y) not in map:
      map[(x, y)] = 0
    map[(x, y)] += 1

  c = 0
  for x in map:
    if map[x] >= 2:
      c += 1

  print(c)