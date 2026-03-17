a=int(input("enter a num:"))
b=int(input("enter a num:"))
c=int(input("enter a num:"))
d=int(input("enter a num:"))
if a>b and a>c and a>d:
    print(a,"is greater")
elif b>c and b>d:
    print(b,"is greater")
elif c>d:
    print(c,"is greater")
else:
    print(d,"is greater")
