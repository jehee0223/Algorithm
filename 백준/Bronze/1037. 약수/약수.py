count=int(input())
measure=list(map(int,input().split(" ")))

min,max=measure[0],measure[0]

for i in range(1,count):
    if(min>measure[i]):
        (min,measure[i])=(measure[i],min)
    if(max<measure[i]):
        (max,measure[i])=(measure[i],max)

print(min*max)