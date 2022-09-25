#the number which all +ve divisors sum except the number itself is equal to the number perfect number
num=int(input("Enter your number to check that is perfect or not  :"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if num==sum:
    print("This is a perfect ")
else:
    print("This number is not perfect.")            