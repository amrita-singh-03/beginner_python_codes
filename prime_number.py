n=int(input("enter a num:"))
i=2
while i<n:
    if n%i==0:
        print("not prime",n)
        break
    i+=1
else:
    print("prime",n)