n=int(input("enter a num:"))
c=0
while n>0:
    n=n//10
    c+=1
print("total digit",c)