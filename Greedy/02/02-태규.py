import sys

S = list(map(int, sys.stdin.readline().strip()))
result = 0

for num in S:
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)