a, b = map(int, input().split())
address = {}
for i in range(a):
    site, pw = input().split()
    address[site]=pw

for i in range(b):
    want=input().strip()
    print(address[want])