X=int(input())

count=1
check=1
a=1
while(check<X):
    if(X-check<count):
        break;
    check+=count
    count+=1

more=X-check
b=count

for _ in range(more):
    a+=1
    b-=1
if(count%2==1):
    print(str(b)+"/"+str(a))
else:
    print(str(a) + "/" + str(b))