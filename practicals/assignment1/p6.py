#character is alphabet or not
 
char= input("Enter a character ")

if len(char)== 1 and ('a'<= char <= 'z' or 'A' <= char <= 'Z'):
    print(char,"is an Alphabet")
else:
    print(char, "is not an Alphabet")
