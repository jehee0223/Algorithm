count=int(input())
nums=list(map(int,input().split()))
result=0
for i in range(count):
    cnt=0
    for j in range(1,1001):
        if nums[i]%j==0 :
            cnt+=1
    if cnt==2:
        result+=1
print(result)