import math
import copy
from functools import reduce

fish = []

with open("input.txt", "r") as f:
  fish = [int(x) for x in f.read().split(",")]
  
def simulate():
  for i in range(len(fish)):
    if fish[i] == 0:
      fish[i] = 6
      fish.append(8)
    else:
      fish[i] -= 1

for i in range(80):
  simulate()
print(len(fish))
