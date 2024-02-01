stick=64

want=int(input())
a=[]

a.append(stick)
while(want<sum(a)):
    stick=a.pop()/2
    a.append(stick)
    if(sum(a)<want):
        a.append(stick)
print(len(a))