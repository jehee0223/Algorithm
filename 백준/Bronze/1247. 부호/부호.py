import sys
for i in range(3):
    N = int(sys.stdin.readline())
    total=0
    for r in range(N):
        num=int(sys.stdin.readline())
        total+=num
    if(total<0):
        print("-")
    elif(total>0):
        print("+")
    else:
        print("0")