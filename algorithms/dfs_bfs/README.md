
# 재귀 함수
## 유클리드 호제법

```python
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

```

## DFS

- 그래프 - 번호가 낮은 인접노드


```python
graph = [
    [], #
    [2,3,8], # 1번 노드에 연결
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
dfs(graph, 1, visited)
```

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

# BFS: 너비우선탐색
- 큐자료 구조
```
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
3. 더이상 2번의 과정을 수행할 수 없을때까지 반복
```



```python
graph = [
    [], #
    [2,3,8], # 1번 노드에 연결
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
bfs(graph, 1, visited)
```

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        # 하나 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visted[i] = True
```




