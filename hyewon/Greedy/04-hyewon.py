n = int(input())
coins = list(map(int, input().split()))
coins.sort()
ans = 1
for c in coins:
    if c > ans:
        break
    ans += c

print(ans)