import sys
input=sys.stdin.readline
count=int(input())
n_list=[0]*10001

for i in range(count):
    n_list[int(input())]+=1

for i in range(len(n_list)):
    if n_list[i]!=0:
        for j in range(n_list[i]):
            print(i)