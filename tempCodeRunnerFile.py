lst=words.split(" ")
lst.sort()

set1=set(lst)
lst1=list(set1)
lst1.sort()
for i in lst1:
    print(i,end=" ")