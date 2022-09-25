def pal(num):
    x1=num[::-1]
    if x1==num:
        print(num,"This is a palindrome number.")
    else:
        print(num,"This is not a pallindrome number.")

num=input("Enter A Number to check pallindrome number or not:")
print(pal(num))
