import copy
peo = list()

# 값 입력받기
for i in range(9):
    peo.append(int(input()))

# 값 2개 뽑기
for i in range(9):
    for j in range(i+1, 9):
        # 값 복사, 합 초기화
        new_peo = copy.deepcopy(peo)
        sum=0
        
        # 삭제할 인덱스 순서
        if i<j:
            del new_peo[j]
            del new_peo[i]
        else:
            del new_peo[i]
            del new_peo[j]
        # 값 합해보기
        for k in range(7):
            sum += new_peo[k]
        # 합이 100이면 정렬
        if sum == 100:
            for i in range(7):
                for j in range(i, 7):
                    if new_peo[i] > new_peo[j]:
                        tmp = new_peo[i]
                        new_peo[i] = new_peo[j]
                        new_peo[j] = tmp
            for k in range(len(new_peo)):
                print(new_peo[k])
            exit(0)