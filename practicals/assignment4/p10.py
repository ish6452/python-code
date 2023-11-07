#output should be 3125 (doubt)

x=int(input("Enter Start : "))
y=int(input("Enter End   : "))
count=1
for i in range(x,y):
    if i%2!=0:
        count=count*i
print(count)
