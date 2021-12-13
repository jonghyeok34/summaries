from collections import deque
# n 정점, m: 간선 개수
N, M = map(int, input().split(" "))

array = [None]
visited = [None]

count = 0
for i in range(N):
    array.append([])
    visited.append(False)

for i in range(M):
    index, link_position = map(int, input().split())
    array[index].append(link_position)
    array[link_position].append(index)

def bfs(start_point):
    queue = deque()
    check_count = 0
    if not visited[start_point]:
        visited[start_point] = True
        queue.append(array[start_point])
        check_count +=1
    while queue:
        next_points = queue.popleft()
        for next_point in next_points:
            if not visited[next_point]:
                visited[next_point] = True
                queue.append(array[next_point])
                check_count +=1
    return check_count

for i in range(1, N+1):
    check_count = bfs(i)
    if check_count>0:
        count +=1

print(count)