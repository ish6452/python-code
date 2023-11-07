x=int(input("Enter Start : "))
y=int(input("Enter End   : "))
for i in range(x,y):
    if i%3==0 and i%5==0 :
        print(i,end=" ")
print()
