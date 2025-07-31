import sys

answer = []
input = sys.stdin.readlines()

for i in range(1,11):
    answer.append(str((i-1)%5+1))

for i in range(int(input[0])):
    if input[i+1].split()==answer:
        print(i+1)