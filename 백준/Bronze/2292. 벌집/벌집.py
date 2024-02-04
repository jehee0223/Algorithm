num=int(input())
a=[1,2]
add=1
while num!=1:
    a.append(a[add]+6*add)
    if num < a[add+1]:
        print(add+1)
        break
    add+=1
if num==1:
    print(1)