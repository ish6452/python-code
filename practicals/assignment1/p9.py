#vowel or consonent

char=input("Enter character : ")
if len(char) == 1 and (char =='a' or char =='e' or char =='i' or char =='o' or char =='u'):
        print(char,"is vowel")
else:
        print(char,"is consonant")
