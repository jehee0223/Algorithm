A,B,V=map(int,input().split())

sub=A-B
nV=V-A
if V==0:
    print('1')
    exit(0)
if V<sub:
    print('2')
    exit(0)
n=nV//sub

if nV%sub>0:
    print(int(n+2))
else:
    print(int(n+1))