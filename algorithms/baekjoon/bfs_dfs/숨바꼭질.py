import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
find_time = 0
visited = [False] * 100001


def find_bro():
    queue = deque()
    queue.append([N])
    global find_time
    while queue:
        positions = queue.popleft()
        new_positions = []
        for position in positions:
            # print(position)
            teleport_pos = position * 2
            walk_pos1 = position - 1
            walk_pos2 = position + 1
            if position == K:
                return
            if 100000 >= walk_pos1 >= 0 and visited[walk_pos1] is False:
                visited[walk_pos1] = True
                new_positions.append(walk_pos1)
            if position < K:
                if 100000 >= walk_pos2 >= 0 and visited[walk_pos2] is False:
                    visited[walk_pos2] = True
                    new_positions.append(walk_pos2)
                if 100000 >= teleport_pos >= 0 and visited[teleport_pos] is False:
                    visited[teleport_pos] = True
                    new_positions.append(teleport_pos)

        if len(new_positions) > 0:
            find_time += 1
            queue.append(set(new_positions))


if N == K:
    find_time = 0
elif N > K:
    find_time = N-K
else:
    find_bro()
print(find_time)
