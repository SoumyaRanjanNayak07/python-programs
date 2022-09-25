# 5=5*4*3*2*1
# n=n*factorial(n-1)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter the number for factorial  :"))
print(factorial(num))            



           
            





