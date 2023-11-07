x=int(input("Enter Start : "))
y=int(input("Enter End   : "))
if x>0 and y>0:
    for i in range(x,y+1):
        print("The ASCII value",i,"is",chr(i))
else:
    print("Wrong Input")
