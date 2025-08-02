import sys

input=sys.stdin.readlines()
string=[]
for i in range(int(input[0])):
    for j in range(len(list(input[i+1])),0,-1):
        string.append(input[i+1][j-2])
        total=''.join(string)
print(total)
