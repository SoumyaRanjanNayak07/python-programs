#take a input string and sort that string charcter
#take input from user and sort that string's characters
def word(str):
    var=sorted(str)
    for i in var:
        print(i,end="")

word_name=input("Enter A word :")
word(word_name)        
