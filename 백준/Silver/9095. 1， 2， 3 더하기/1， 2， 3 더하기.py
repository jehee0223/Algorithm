case=int(input())

for _ in range(case):
    num=int(input())
    a=[0]*(num+1)

    for i in range(1,num+1):
        if i==1:
            a[i]=1
        elif i==2:
            a[i]=2
        elif i==3:
            a[i]=4
        else:
            a[i]=a[i-1]+a[i-2]+a[i-3]
    print(a[i])
