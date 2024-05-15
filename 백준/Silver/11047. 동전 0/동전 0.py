K, N = map(int, input().split())

coin = list()

for _ in range(K):
    coin.append(int(input()))

coin = coin[::-1]
cnt = 0
for i in coin:
    cnt += N // i
    N = N % i
print(cnt)
