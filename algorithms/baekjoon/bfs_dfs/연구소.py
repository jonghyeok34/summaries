from collections import deque
import time
# n = row count, m = col count
n,m = map(int, input().split(" "))
labatory = []
start_points = []
clean_spots = []
# 처음 안전영역
intial_safe_count = 0
max_safe_count = 0
# 임시로 3개 point 저장 
temp_wall_map = []
# 벽 3개 기록
history = {}

dRow = [0, 0, 1,-1]
dCol = [1,-1,0,0]
s = time.time()
for i in range(n):
    labatory.append([int(x) for x in input().split(" ", m)])
    temp_wall_map.append([0]* m)
    for j in range(len(labatory[i])):
        if labatory[i][j] ==2:
            start_points.append((i,j))
        if labatory[i][j] ==0:
            clean_spots.append((i,j))
            intial_safe_count +=1

iterate_count = 0

def make_viral():
    queue = deque()
    global temp_wall_map
    global max_safe_count
    global start_points
    # 시작 지점
    # for start_point in start_points:
    queue.append(start_points)
    infected_count = 0
    visited = {}
    global iterate_count
    while queue:
        
        # row, col= queue.popleft()
        points = queue.popleft()
        # print(point)
        next_points = []
        for point in points:
            print(points)
            row = point[0]
            col = point[1]
            for i in range(4):
                nRow = row + dRow[i]
                nCol = col + dCol[i]
                # 범위 안의
                if 0<= nRow < n and 0<= nCol < m :
                    # 방문하지 않았고 무감염 지역
                    if visited.get((nRow,nCol)) is None and temp_wall_map[nRow][nCol] ==0 and labatory[nRow][nCol] ==0:
                        # print(nRow, nCol)
                        visited[(nRow,nCol)] = True
                        queue.append((nRow, nCol)) 
                        infected_count +=1
                        iterate_count +=1
                        next_points.append((nRow,nCol))
                        if max_safe_count > intial_safe_count - infected_count:
                            return max_safe_count
        if len(next_points)>0:
            queue.append(next_points)    
    return intial_safe_count - infected_count
# iterate and position temp wall
clean_spot_count = len(clean_spots)

# 3 spots for 
for i in range(clean_spot_count):
    for j in range(clean_spot_count):
        for k in range(clean_spot_count):
            row1,col1 = clean_spots[i]
            row2,col2 = clean_spots[j]
            row3,col3 = clean_spots[k]
            
            if i==j or i==k or j ==k:
                continue
            elif labatory[row1][col1] !=0 or labatory[row2][col2]!=0 or labatory[row3][col3]!=0:
                continue
            else:
                
                temp_wall_map[row1][col1] = 1
                temp_wall_map[row2][col2] = 1
                temp_wall_map[row3][col3] = 1
                
                # print(clean_spots[i], clean_spots[j], clean_spots[k])
                max_safe_count = make_viral()
                
                # print(max_safe_count)
                # temp wall reset
                temp_wall_map[row1][col1] = 0
                temp_wall_map[row2][col2] = 0
                temp_wall_map[row3][col3] = 0
                
        # save history
e = time.time()
print(e-s)
# 추가 벽 개수 3개 빼주기
print("iterater_Count:",iterate_count)
print(max_safe_count- 3)
# count 2s and 