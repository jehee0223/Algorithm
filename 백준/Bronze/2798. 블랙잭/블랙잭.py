count,want=map(int,input().split(" "))
num=list(map(int,input().split(" ")))

similar=300000
result=0
for i in range(count-2):
    for j in range(i+1,count-1):
        for k in range(j+1,count):
            sum=num[i]+num[j]+num[k]
            if want-sum>=0 and want-sum<similar:
                similar=want-sum
                result=sum
print(result)