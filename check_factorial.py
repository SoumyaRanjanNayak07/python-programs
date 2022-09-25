def fact(n):
    if n==1&n==0:
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter the number you want the factorial  :"))
print(f"factorial of {num} is {fact(num)} ")
