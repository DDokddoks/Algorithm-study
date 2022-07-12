from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

shortestPath = [-1] * (n + 1)
shortestPath[x] = 0

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        cur = q.popleft()
        for loc in graph[cur]:
            if shortestPath[loc] == -1:
                q.append(loc)
                shortestPath[loc] = shortestPath[cur] + 1

bfs(x)

flag = 0
for i in range(1, n + 1):
    if shortestPath[i] == k:
        print(i)
        flag = 1
if flag == 0:
    print(-1)