import math
while True:
    num=list(map(int,input().split()))
    if num[0]==0 and num[1]==0 and num[2]==0:
        exit(0)
    num.sort()
    if math.pow(num[2],2)==math.pow(num[1],2)+math.pow(num[0],2):
        print('right')
    else:
        print('wrong')