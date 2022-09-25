def pallindrome_check(word):
    reverse_word=word[::-1]
    if word==reverse_word:
        print("IT IS A PALLINDROME WORD")
    else:

        print("Not a pallindrome word")

a=str(input("Enter your Word :"))
pallindrome_check(a)
 