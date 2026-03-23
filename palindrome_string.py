str1=input("enter a string:")
rev=''
for ch in str1:
    rev=ch+rev
if rev==str1:
    print(str1,"is palindrome")
else:
    print(str1,"is not palindrome")