cnt = int(input())

times = list(map(int, input().split()))

times.sort()
total=0
for i in range(cnt):
    total+=sum(times[0:i+1])
print(total)