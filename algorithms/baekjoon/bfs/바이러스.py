'''
point_count = int(input())
link_count = int(input())

graph = {}
check = {}

for i in range(link_count):
    start, end = [int(x) for x in input().split()]
    if not graph.get(start):
        graph[start] =[]
    if not graph.get(end):
        graph[end] = []
    graph[start].append(end)
    graph[end].append(start)
    check[(start,end)] = False
    check[(end,start)] = False
    
count = 0
print(graph)
print(check)

def dfs(previous, current):
    if check.get((previous,current)) is False:
        print(previous, current)
    
        if current != 1:
            global count
            check[(previous,current)] = True
            check[(current, previous)] = True
            count +=1
        for next in graph[current]:
            dfs(current, next)

dfs(1,2)
print(count)
'''
point_count = int(input())
link_count = int(input())

graph = {}
check = {}

for i in range(link_count):
    start, end = [int(x) for x in input().split()]
    if not graph.get(start):
        graph[start] = []
    if not graph.get(end):
        graph[end] = []
    graph[start].append(end)
    graph[end].append(start)

for j in range(point_count):
    check[j+1] = False

count = 0


def dfs(current):
    if check.get(current) is False:
        if current != 1:
            global count
            check[current] = True
            count += 1
        for next in graph[current]:
            dfs(next)


dfs(1)
print(count)
