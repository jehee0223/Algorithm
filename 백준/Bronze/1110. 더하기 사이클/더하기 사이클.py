num=int(input())
first=num
cnt=0
while 1:
    a=num//10
    b=num%10
    num=b*10+(a+b)%10
    cnt+=1
    if first==num:
        break
print(cnt)