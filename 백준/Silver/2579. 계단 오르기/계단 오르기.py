# 풀이 실패
# DP문제
# 이제 DP 느낌은 조금 알 것 같음

N = int(input())
dp = [0] * (N+1)
point = [0] * (N+1)
for i in range(1, N+1):
    point[i] = int(input())
if N==1:
    print(point[1])
    exit()
elif N==2:
    print(sum(point[:3]))
    exit()
dp[1] = point[1]
dp[2] = point[1]+point[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i])

print(dp[-1])