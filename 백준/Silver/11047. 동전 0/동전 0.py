K, N = map(int, input().split())

coin = list()

for _ in range(K):
    coin.append(int(input()))
cnt = 0
max=K
while (True):
    if N > coin[max-1]:
        a = N / coin[max-1]
        cnt += int(a)
        N -= cnt * coin[max-1]
    elif N == 0:
        break
    elif N < coin[K - 1]:
        K -= 1
    elif N >= coin[K - 1]:
        N -= coin[K - 1]
        cnt += 1
print(cnt)