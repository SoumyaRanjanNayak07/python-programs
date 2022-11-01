words = input("Enter your words with whitespaces: ")
#ram is  not a  guy ram is a
lst = words.split(" ")
lst.sort()
#lst =['ram', is , not ,a  guy ram is a]

set1 = set(lst)
list1 = list(set1)
list1.sort()
for i in list1:
  print(i, end=" ")