num=int(input())
success=False
for i in range(1,num+1):
    k=list()
    sum=0
    for j in str(i):
        sum+=int(j)
    if i+sum==num:
        success=True
        break
if success==False:
    print('0')
else:
    print(i)