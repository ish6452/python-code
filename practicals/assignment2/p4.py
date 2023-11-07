#take a no from use and check if available in list
List1=[10,20,30,40,50]
num =int(input("Enter value : "))
for x in List1:
    if x==num:
        print(num,"is available")
        break
else:
    print(num,"not available")
