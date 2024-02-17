import sys
count=int(sys.stdin.readline())
nums=list()

for i in range(count):
    nums.append(int(sys.stdin.readline()))

nums=list(set(nums))
nums.sort()
for i in range(count):
    print(nums[i])
