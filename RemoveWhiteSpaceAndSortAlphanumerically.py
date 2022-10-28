words=input("Enter your words or sentence with white spaces and duplicate words:")
words=words.lower()

lst=words.split(" ")
lst.sort()

set1=set(lst)
lst1=list(set1)
lst1.sort()
for i in lst1:
    print(i,end=" ")