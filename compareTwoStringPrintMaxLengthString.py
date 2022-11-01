def string(str1, str2):
  count1 = len(str1)
  count2 = len(str2)
  if count1 > count2:
    print("Maximum length string is:", str1)
  elif count1 < count2:
    print("Maximum length string is:", str2)
  else:
    print("Both string length is  same: ", str1, str2, sep="\n")


string1 = input("Enter your first string/word:")
string2 = input("Enter your second string/word:")

string(string1, string2)