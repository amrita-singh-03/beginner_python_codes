s=input("enter a string")
new=''
for ch in s:
    if ch!=' ':
        new+=ch
print("without space:",new)