import math
import copy
from functools import reduce

def z(b, pi, v):
  st = [pi]
  c = 0
  while len(st) > 0:
    p = st.pop(0)
    x = p[0]
    y = p[1]
    if p in v or b[y][x] == 9:
      continue

    v.append(p)
    c += 1

    if x > 0:
      st.append((x-1, y))
    if y > 0:
      st.append((x, y-1))
    if x < len(b[y])-1:
      st.append((x+1, y))
    if y < len(b)-1:
      st.append((x, y+1))

  return c

with open("input.txt", "r") as f:
  b = []
  # iterate over every line in a file
  for l in f.read().split("\n"):
    b.append([int(x) for x in l])

  v = []
  r = []
  for y in range(len(b)):
    for x in range(len(b[y])):
      r.append(z(b, (x, y), v))
  
  r = sorted(r)[::-1]
  print(r[0] * r[1] * r[2])

