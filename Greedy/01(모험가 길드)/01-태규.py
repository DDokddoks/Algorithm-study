import sys

N = int(sys.stdin.readline())
fears = list(map(int, sys.stdin.readline().split()))
fears.sort()
result = 0
count = 0

for item in fears:
    count += 1
    if count >= item:
        result += 1
        count = 0
print(result)