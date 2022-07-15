n, m = map(int, input().split())
balls = list(map(int, input().split()))
counts = [0] * (m + 1)

for b in balls:
    counts[b] += 1

answer = 0
print(counts)
for i in range(1, m + 1):
    a = counts[i]
    b = sum(counts[i + 1:m + 1])
    answer += a * b

print(answer)