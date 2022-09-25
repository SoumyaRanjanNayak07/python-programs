#To print the fibonacci series of n numbers.
first_num=int(input("Enter the first number :"))
second_num=int(input("Enter the second number :"))
num_of=int(input("Enter the length number you want to print fibonacci  series :"))
print(first_num,second_num,end=" ")
while num_of-2:
    fibo_num=first_num+second_num
    first_num=second_num
    second_num=fibo_num
    print(fibo_num,end=" ")
    num_of=num_of-1