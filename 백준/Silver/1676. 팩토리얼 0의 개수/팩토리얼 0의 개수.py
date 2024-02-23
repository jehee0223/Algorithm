N=int(input())
a=[]
result=1
cnt=0
for i in range(1,N+1):
    result*=i
for i in str(result):
    a.append(i)
for i in range(len(a)-1,-1,-1):
    if a[i]!='0':
        break
    else:
        cnt+=1
print(cnt)