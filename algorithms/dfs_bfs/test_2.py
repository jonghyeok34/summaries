from collections import deque

n, m = 5,6
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]
dx = [-1, 1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간 벗어남
            if nx <0 or nx >=n or ny <0 or ny >=m:
                continue
            # graph 0
            if graph[nx][ny] ==0:
                continue
            # ?? 무슨 의미
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))