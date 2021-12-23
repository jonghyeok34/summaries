from collections import deque
# n : max row, m : max col
n, m = map(int, input().split( " ",2))

maze = []
check = {}
dRow = [0,0,1,-1]
dCol = [1,-1,0,0]
for i in range(n):
    maze.append([int(x) for x in input()])

def search_maze(firstRow, firstCol):
    queue = deque()
    queue.append([(firstRow, firstCol)])
    count = 0
    while queue:
        # print(queue)
        count +=1
        rowColList = queue.popleft()
        # print(rowColList)
        nextList = []
        for rowCol in rowColList:
            row = rowCol[0]
            col = rowCol[1]
            if row == n and col == m:
                return count
            for i in range(4):
                nRow = row + dRow[i]
                nCol = col + dCol[i]
                
                if 1<=nRow<=n and 1<=nCol<=m and check.get((nRow, nCol)) is None:
                    if maze[nRow-1][nCol-1] ==1:
                        # queue.append((nRow, nCol))
                        nextList.append((nRow, nCol))
                        check[(nRow,nCol)] = True
        if len(nextList)>0:
            queue.append(nextList)
    return count

print(search_maze(1,1))