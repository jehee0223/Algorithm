import sys
works = {'Re':0,'Pt':0,'Cc':0,'Ea':0,'Tb':0,'Cm':0,'Ex':0}
count=0
input=sys.stdin.read()

for i in (input.split()):
    if i in works:
        works[i]+=1
    count+=1

for i in works:
    print(f'{i} {works[i]} {format(works[i]/count,".2f")}')
print(f'Total {count} 1.00')