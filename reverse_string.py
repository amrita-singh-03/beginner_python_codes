a=input("enter a string")
rev=''
for ch in a:
    rev=ch+rev
print(rev)

#method-2
x=input("enter a string")
rev=x[::-1]
print(rev)