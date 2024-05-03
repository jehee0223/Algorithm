room = []
sum = []

case = int(input())
for i in range(case):
    floor = int(input())
    num = int(input())
    room.append([floor, num])

for k in range(case):
    for i in range(room[k][0]):
        for j in range(1, room[k][1] + 1):
            if i == 0:
                sum.append(j)
            if j == 1:
                sum[0] = 1
            else:
                sum[j - 1] += sum[j - 2]
    print(sum[-1])
    sum=[]