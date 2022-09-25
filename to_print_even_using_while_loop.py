# To display even number from m to n using while loop

first_num=int(input("Enter the first number"))
last_num=int(input("Enter the last number"))
'''
if first_num%2!=0:
    first_num=first_num+1

while first_num<=last_num:
    print(first_num)
    first_num=first_num+2
print("end of value") 
'''  
while first_num<=last_num:
    if first_num%2==0:
        print(first_num)
    else:
        first_num=first_num+1
        print(first_num)
    
    first_num=first_num+2     