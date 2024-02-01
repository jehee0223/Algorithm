num=list(map(int,input().split()))

# 가장 작은 수부터 탐색
for i in range(1,1000000):
    cnt=0
    # i가 j의 배수이면 cnt++
    for j in range(5):
        if(i%num[j]==0):
            cnt+=1
    # cnt가 3회 이상이면 그게 정답
    if(cnt>=3):
        drainage=i
        break
print(drainage)