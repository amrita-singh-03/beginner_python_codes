num=int(input("enter a num:"))
lenth=len(str(num))
temp=num
out=0
while num>0:
    digit=num%10
    out+=digit**lenth
    num=num//10
if out==temp:
    print('armstrong num')
else:
    print("not armstrong")
