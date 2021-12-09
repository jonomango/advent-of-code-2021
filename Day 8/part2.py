import math
import copy
from functools import reduce



with open("input.txt", "r") as f:
  c = 0

  # iterate over every line in a file
  for l in f.read().split("\n"):
    a, b = l.split(" | ")
    a = a.split(" ")
    b = b.split(" ")
    
    n = {}
    for x in a:
      if len(x) == 7:
        n[8] = x
      if len(x) == 4:
        n[4] = x
      if len(x) == 3:
        n[7] = x
      if len(x) == 2:
        n[1] = x

    n[9] = [y for y in a if y not in n.values() and len(y) == 6 and sum(c in y for c in n[4]) == 4][0]
    n[0] = [y for y in a if y not in n.values() and len(y) == 6 and all(c in y for c in n[1])][0]
    n[6] = [y for y in a if y not in n.values() and len(y) == 6][0]
    n[3] = [y for y in a if y not in n.values() and all(c in y for c in n[1])][0]
    n[5] = [y for y in a if y not in n.values() and all(c in n[9] for c in y)][0]
    n[2] = [y for y in a if y not in n.values()][0]

    inv = { ''.join(sorted(v)): k for k, v in n.items() }

    s = 0
    for x in b:
      s = s * 10 + inv[''.join(sorted(x))]
    c += s
    
  print(c)

