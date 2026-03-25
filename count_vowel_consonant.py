s=input("enter a string: ")
vowel=0
consonant=0
vow=''
cons=''
for ch in s:
    if ch in 'aeiouAEIOU':
        vowel+=1
        vow+=ch
    else:
        consonant+=1
        cons+=ch
print(vowel,end=" ")
print("vowel",vow)
print(consonant,end=" ")
print("consonant",cons)
