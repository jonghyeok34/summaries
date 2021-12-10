
from collections import deque

N, M, V = [int(x) for x in input().split(" ")]

graph = [None]
dfs_check = [True]
bfs_check = [True]
dfs_result = []
bfs_result = []

for i in range(N):
    graph.append([])

for i in range(M):
    _from, _to = [int(x) for x in input().split(" ")]
    graph[_from].append(_to)
    graph[_to].append(_from)

for i in range(1, len(graph)):
    graph[i] = sorted(graph[i])

for i in range(N):
    dfs_check.append(False)
    bfs_check.append(False)


def dfs(start):
    if dfs_check[start] is False:
        print(start, end=' ')
        dfs_check[start] = True

        for nextStart in graph[start]:
            dfs(nextStart)


def bfs():
    queue = deque()
    queue.append(V)

    while queue:
        start = queue.popleft()
        print(start, end=' ')
        bfs_check[start] = True
        for next in graph[start]:
            if bfs_check[next] is False:
                bfs_check[next] = True
                queue.append(next)


# 1. dfs
dfs(V)
print()
bfs()
