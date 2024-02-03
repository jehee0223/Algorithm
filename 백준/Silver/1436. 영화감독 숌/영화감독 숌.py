num = int(input())
name = 666
check = list()

while True:
    tmp=name
    each_num=list()
    for i in range(len(str(name))):
        each_num.append(tmp%10)
        tmp//=10
    # 6이 3개 연속이면 list에 추가
    for j in range(len(each_num)-2):
        if each_num[j]==6 and each_num[j+1]==6 and each_num[j+2]==6:
            check.append(name)
            break
    name+=1
    # list의 길이가 원하는 index번호까지 있다면 탈출
    if len(check)==num:
        break
print(check[num-1])