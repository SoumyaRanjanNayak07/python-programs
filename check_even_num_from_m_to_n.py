#Check Even Numbers from a given number to another number

m=int(input("Enter your starting point value"))
n=int(input("Enter your starting point value"))


for i in range(m,n+1):
    if(i%2==0):
        print(i ,end=" ,")