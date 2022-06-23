import sys

n, m = map(int, sys.stdin.readline().split())
balls = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(n):
    for j in range(i, n):
        if balls[i] != balls[j]:
            result += 1
print(result)