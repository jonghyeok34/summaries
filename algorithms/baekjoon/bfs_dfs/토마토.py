from collections import deque
# M = col count, N = row count
M, N = map(int, input().split(" ", 2))


# 전체 토마토 개수
tomatoes_count = 0
# 시작점 - 익어있는 토마토
start_points = []
box = []  # 토마토 박스
check = []  # check 여부 [i,j]
# 방향 vector
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]
for i in range(N):
    box.append(list(map(int, input().split(" ", M))))
    check.append([False]*M)
    for j in range(M):
        if box[i][j] >= 0:
            tomatoes_count += 1
        if box[i][j] >= 1:
            start_points.append((i, j))

min_day = 0


def ripe_tomatoes(start_points: list):
    queue = deque()
    # for start_point in start_points:
    queue.append(start_points)
    global min_day
    while queue:
        points = queue.popleft()
        new_points = []
        for point in points:
            row, col = point
            box[row][col] += 1
            for i in range(4):
                new_row = row + dy[i]
                new_col = col + dx[i]
                if 0 <= new_row < N and 0 <= new_col < M and box[new_row][new_col] == 0 and check[new_row][new_col] is False:
                    check[new_row][new_col] = True
                    new_points.append((new_row, new_col))
        if len(new_points) > 0:
            queue.append(new_points)
            min_day += 1
        # dx


def has_unrippen():
    has_unrippen = False
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                has_unrippen = True
                break
    return has_unrippen


# 진행
ripe_tomatoes(start_points=start_points)

result = 0
# 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1
if tomatoes_count == len(start_points):
    result = 0
elif has_unrippen():
    result = -1
else:
    result = min_day
print(result)
