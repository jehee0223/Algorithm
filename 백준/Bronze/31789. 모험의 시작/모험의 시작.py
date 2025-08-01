import sys

check="NO"
input=sys.stdin.readlines()
money, enemy = map(int,input[1].split())
for i in range(2,int(input[0])+2):
    price, damage = map(int,input[i].split())
    if price <= money and damage > enemy:
        check="YES"
        break
print(check)