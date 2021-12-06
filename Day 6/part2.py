import math
import copy
from functools import reduce

fish = [0 for _ in range(9)]

with open("input.txt", "r") as f:
  for x in f.read().split(","):
    fish[int(x)] += 1
  
def simulate(f):
  n = f[0]
  f = f[1:]
  f.append(n)
  f[6] += n
  return f

for i in range(256):
  fish = simulate(fish)
print(sum(fish))


