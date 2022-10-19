def RemainderArr(arr, d, n):
  MulArr = 1
  for i in range(n):
    MulArr *= arr[i]
  return MulArr % d


num = int(input("Enter the number of terms for array length:"))

arr1 = []
for i in range(num):
  k = float(input("Enter the array values:"))
  arr1.append(k)

div = float(input("Enter the Divisor :"))

print(RemainderArr(arr1, div, num))
