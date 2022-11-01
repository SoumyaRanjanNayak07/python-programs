string = input("Enter Your sentence: ")
lst = string.split()
lst = sorted(lst)
lst1 = []
for i in lst:
  if i not in lst1:
    lst1.append(i)

for j in lst1:
  print(f" {j}:{lst.count(j)}")