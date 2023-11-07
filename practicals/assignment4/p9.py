x=int(input("Enter Start : "))
y=int(input("Enter End   : "))
count=0
for i in range(x,y):
    if i<0:
        count=count+1
print(count)


