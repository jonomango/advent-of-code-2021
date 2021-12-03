import math
import copy
from functools import reduce


arr = []
with open("input.txt", "r") as file:
  # iterate over every line in a file
  for line in file.read().strip().split("\n"):
    arr.append(line)

def freq(arr):
  f = [0 for _ in range(len(arr[0]))]
  for line in arr:
    for i in range(len(line)):
      if line[i] == '1':
        f[i] += 1
      elif line[i] == '0':
        f[i] -= 1
  return f

arr3 = arr.copy()

for i in range(len(arr[0])):
  arr2 = arr3.copy()
  arr3 = []
  f = freq(arr2)
  if f[i] >= 0:
    for a in arr2:
      if a[i] == '1':
        arr3.append(a)
  else:
    for a in arr2:
      if a[i] == '0':
        arr3.append(a)

  if len(arr3) == 1:
    break

o = int(arr3[0], 2)

arr3 = arr.copy()

for i in range(len(arr[0])):
  arr2 = arr3.copy()
  arr3 = []
  f = freq(arr2)
  if f[i] < 0:
    for a in arr2:
      if a[i] == '1':
        arr3.append(a)
  else:
    for a in arr2:
      if a[i] == '0':
        arr3.append(a)

  if len(arr3) == 1:
    break

c = int(arr3[0], 2)
print(o * c)