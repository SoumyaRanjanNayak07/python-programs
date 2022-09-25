#program_to_count_letters_and_digits_of_string_from_console
string=input("Enter your string to  count all Letters and digits: ")
letter=0
digit=0
for i in string:
    if i.isalpha()==True:
        letter+=1
    if i.isdigit()==True:
        digit+=1
print(f" Total letters:{letter} ")
print(f"Total digits :{digit}")

    
    




