from collections import deque

link = 0

n = 4
m = 5
graph = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]

def dfs(x,y):
    # 범위를 벗어남
    if x<= -1 or x >=n or y <=-1 or y >=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x +1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)