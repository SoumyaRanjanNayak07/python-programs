#Check armostrong number which entered by user
num=int(input("Enter the number you want to check the amstrong  :"))
s=0
temp=num
while temp>0:
    c =temp%10
    s +=c**3
    temp //=10
if num == s:
    print(num,"This is Armstrong number")
else:
    print(num,"This is not a armstrong ")