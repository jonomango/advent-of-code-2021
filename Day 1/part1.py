arr = []

with open("input.txt", "r") as f:
  for line in [l.replace("\n", "") for l in f.readlines()]:
    arr.append(int(line))

counter = 0
for i in range(1, len(arr)):
  if (arr[i] > arr[i-1]):
    counter += 1

print("solution:", counter)