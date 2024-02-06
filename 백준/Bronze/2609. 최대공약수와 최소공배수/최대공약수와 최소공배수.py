a,b=list(map(int,input().split()))
c=list()
na=list()
nb=list()
nab=list()
num=2
low=1
great=1
while True:
    if a%num==0 and b%num==0:
        c.append(num)
        a//=num
        b//=num
    elif a%num==0 and b%num!=0:
        na.append(num)
        a//=num
    elif a%num!=0 and b%num==0:
        nb.append(num)
        b//=num
    else:
        num+=1
        if a==1 and b==1:
            break
nab=na+nb
for i in c:
    low*=i
for j in nab:
    great*=j
great*=low
print(low,great)