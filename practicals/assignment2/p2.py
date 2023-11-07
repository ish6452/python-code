#to determine whether th triangle is right angle r not 
a=int(input("Enter angle 1: "))
b=int(input("Enter angle 2: "))
c=int(input("Enter angle 3: "))

if(a==90 and (a+b+c)==180) or (b==90 and (a+b+c)==180) or (c==90 and (a+b+c)==180):
    print("Right Angled Triangle ")
else:
    print("Not Right Angled Triangle ")
