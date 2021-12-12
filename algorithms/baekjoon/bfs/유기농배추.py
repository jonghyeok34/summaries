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

    def dfs(x,y):
        if check[y][x] is False:
            global count
            check[y][x] = True
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny <0 or nx>=M or ny>=N:
                    continue
                if field[ny][nx] ==1 and check[ny][nx] is False:
                    count+=1
                    dfs(nx,ny)
    space_count = 0
    for y in range(N):
        for x in range(M):
            count = 0
            dfs(x, y)
            if count >0:
                space_count+=1
    counts.append(space_count)

for count in counts:
    print(count)
