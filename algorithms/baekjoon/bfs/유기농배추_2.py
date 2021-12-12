from collections import deque
T = int(input())
counts = []
count = 0
dx = [0,1,-1,0]
dy = [1,0,0,-1]

for i in range(T):
    M, N, K =[int(x) for x in input().split(" ")]

    field = []
    check = []

    for i in range(N):
        field.append([0]*M)
        check.append([False]*M)
    # print(field)
    # 배추
    for i in range(K):
        x, y = [int(a) for a in input().split(" ")]
        field[y][x] = 1

    def bfs():
        queue = deque()
        queue.append(0,0)
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if check[y][x] is False:
                    queue.append(nx,ny)
                

    space_count = 0
    for y in range(N):
        for x in range(M):
            count = 0
            bfs(x, y)
            if count >0:
                space_count+=1
    counts.append(space_count)

for count in counts:
    print(count)
