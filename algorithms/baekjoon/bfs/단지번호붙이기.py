
n = int(input())
# 
location = []
for i in range(n):
    location.append([int(x) for x in input()])

check = []
for i in range(n):
    check.append([False]*n)
    
dX = [-1,0,0,1]
dY = [0, 1,-1,0]
dongs = []
count = 0

def dfs( x, y):
    if check[x][y] is False:
        check[x][y] = True
        global count
        for i in range(4):
            nx = x + dX[i]
            ny = y + dY[i]
            if nx <0 or ny <0 or nx>= n or ny>= n:
                continue
            if location[nx][ny] == 1 and check[nx][ny] is False:
                location[nx][ny] = 1 + len(dongs)
                count +=1
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        count =0
        dfs(i, j)
        if count >0:
            dongs.append(count)
dongs = sorted(dongs)
dong_count =len(dongs)
print(dong_count)
for i in range(dong_count):
    print(dongs[i])