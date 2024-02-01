def add(a, b):
    return a + b
def div(a, b):
    return a // b
def mod(a,b):
    return a % b
def mul(a, b):
    return a*b
def sub(a,b):
    return a-b

a, b = map(int, input().split())

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(mod(a,b))
