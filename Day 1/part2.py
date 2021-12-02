arr = []

with open("input.txt", "r") as f:
  for line in [l.replace("\n", "") for l in f.readlines()]:
    arr.append(int(line))

arr2 = []
for i in range(0, len(arr) - 2):
  arr2.append(arr[i] + arr[i + 1] + arr[i + 2])

counter = 0
for i in range(1, len(arr2)):
  if (arr2[i] > arr2[i - 1]):
    counter += 1

print("solution:", counter)