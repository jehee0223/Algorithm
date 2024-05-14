import sys

nums = set()
count = int(input())

for _ in range(count):
    check = sys.stdin.readline().strip().split()
    if len(check) == 1:
        if check[0] == 'all':
            nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                    '19', '20'}
        else:
            nums = set()

    if check[0] == 'add':
        nums.add(check[1])
    elif check[0] == 'remove':
        nums.discard(check[1])
    elif check[0] == 'toggle':
        if check[1] in nums:
            nums.discard(check[1])
        else:
            nums.add(check[1])
    elif check[0]=='check':
        if check[1] in nums:
            print("1")
        else:
            print("0")