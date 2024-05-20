# 풀이 실패
# 너비 우선 탐색(BFS)
# 루트 노드에서 시작해 인접한 노드를 먼저 탐색하는 방법
# 큐(Queue) 사용 -> FIFO

case=int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = [(x,y)]
    ground[x][y] = 0

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if ground[nx][ny] == 1 :
                queue.append((nx,ny))
                ground[nx][ny] = 0

for _ in range(case):
    cnt=0
    M,N,K=map(int,input().split())
    ground=[[0]*N for _ in range(M)]
    for i in range(K):
        x,y=map(int,input().split())
        ground[x][y]=1
    for a in range(M):
        for b in range(N):
            if ground[a][b] == 1:
                BFS(a, b)
                cnt += 1
    print(cnt)