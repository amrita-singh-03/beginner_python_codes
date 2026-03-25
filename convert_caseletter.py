s=input("enter a name")
for ch in s:
    if 'A'<=ch<='Z':
        print(ch.lower(),end=" ")
    elif 'a'<=ch<='z':
        print(ch.upper(),end=" ")
        