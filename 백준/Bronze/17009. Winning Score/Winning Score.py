import sys
shoots=sys.stdin.read()
A=B=cnt=0

for i in shoots.split():
    i=int(i)
    if cnt<3:
        A+=i*(3-cnt)
    else:
        B+=i*(6-cnt)
    cnt+=1

print("A" if A>B else "B" if A<B else "T")