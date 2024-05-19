cnt = int(input())

times = list(map(int, input().split()))

times.sort()
total = list()
for i in range(cnt):
    if(i==0):
        total.append(times[i])
    else:
        total.append(total[i-1]+times[i])
print(sum(total))