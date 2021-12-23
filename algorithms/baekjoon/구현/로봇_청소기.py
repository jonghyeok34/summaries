import time
# n - row count, m = col count

n, m = map(int, input().split(" ", 2))
# r,c - point / direction = 0 - n,
r, c, d = map(int, input().split(" ", 3))

dR = [1, 0, -1, 0]
dC = [0, 1, 0, -1]
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
opposite_direction = {
    NORTH: SOUTH,
    EAST: WEST,
    SOUTH: NORTH,
    WEST: EAST
}
# def play_robot():
CLEANED = 2
WALL = 1
place = []
for i in range(n):
    place.append([int(x) for x in input().split(" ", m)])

count = 0
print(place)

# 현재 위치를 청소한다.
if place[r][c] == 0:
    place[r][c] = CLEANED
    print("clean", r, c)
    count += 1

while True:
    print(r, c, count)
    # print(place)
    # time.sleep(0.3)

    find_uncleaned = False
    
    # 2번
    for j in range(4):
        # 왼쪽 방향
        d = abs( (d- 1)%4)
        nr = r + dR[d]
        nc = c + dC[d]
        if 1 <= nr < n-1 and 1 <= nc < m-1:
            # 청소할 공간이 없다면, 회전하고 2번으로 돌아간다.
    
            if place[nr][nc] in [1,2]:
                continue
            # 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            else:
                # 현재 위치를 청소한다.
                place[nr][nc] = CLEANED
                print("clean", nr, nc)
                count += 1
            
                r = nr
                c = nc
                find_uncleaned = True
                break
    if find_uncleaned:
        continue

    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    opposite_d = opposite_direction[d]
    nr = r + dR[opposite_d]
    nc = c + dC[opposite_d]
    if 0 <= nr < n and 0 <= nc < m:
        r = nr
        c = nc
        if place[nr][nc] == WALL:
            break

            # place[r][c]
for p in place:
    print(p)
print(count)
