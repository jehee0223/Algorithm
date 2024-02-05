count=int(input())

score=list(map(int,input().split()))

score.sort()

result=sum(score)/len(score)/score[count-1]*100

print(result)