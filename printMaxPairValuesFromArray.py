def MaxPair(arr):
  #Array Length
  arrlength = len(arr)
  if arrlength < 2:
    print("There is no pair")
    return
  x = arr[0]
  y = arr[1]
  for i in range(0, arrlength):
    for j in range(i + 1, arrlength):
      if arr[i] * arr[j] > x * y:
        x = arr[i]
        y = arr[j]
  return x, y


arr = [23, 56, 67, 36, 23, 47, 44, 3, 46, 6]
print(MaxPair(arr))