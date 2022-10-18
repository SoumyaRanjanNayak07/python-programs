def recursion(n):
  if n <= 1:
    return n
  else:
    return recursion(n - 1) + recursion(n - 2)


numterms = int(input("Enter the number of terms :"))
if numterms <= 0:
  print("Enter a positive number:")
else:
  for i in range(numterms):
    print(recursion(i))