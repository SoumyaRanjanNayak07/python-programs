#Check armostrong number which entered by user
# num=int(input("Enter the number you want to check the amstrong  :"))
# s=0
# temp=num
# while temp>0:
#     c =temp%10
#     s +=c**3
#     temp //=10
# if num == s:
#     print(num,"This is Armstrong number")
# else:
#     print(num,"This is not a armstrong ")


#Check armostrong number which entered by user
# e.g of amstrong numbers 0,1,153,370,371,407
num=int(input("Enter the number to check for Amstrong:"))
sum=0
temp=num
if temp>0:
    while(temp>0):
    
        c=temp%10
        sum=sum+c*c*c
        temp=temp//10
        # print(num)

    # print(sum)
    if num==0 or num==1:
        print("It is Amstrong Number. ",num)
    elif sum==num:
        print("It is Amstrong Number. ",sum)   
    else:
        print("It is not a amstrong number.",num)   