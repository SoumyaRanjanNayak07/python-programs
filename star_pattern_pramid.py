num=int(input("Enter the number to print star piramid"))
m=(2*num)-2
for i in range(0,num):
    for j in range(0,num):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print("*", end=" ")
    print(" ")