# # 재귀를 이용한 풀이
# import sys

# N = int(sys.stdin.readline())
# coins = list(map(int, sys.stdin.readline().split()))
# coins.sort()

# count = 0

# def check(count, index):
#     if count == 0:
#         return True    
#     for i in reversed(range(index)):
#         if coins[i] <= count:
#             if check(count-coins[i], i): 
#                 return True
#             else:
#                 if i == 0: return False
#     if count != 0:
#         return False

# while True:
#     count += 1
#     if check(count, N) == False:
#         print(count)
        
# 모범 풀이
n = int(input())
coins = list(map(int, input().split()))
coins.sort()
ans = 1
for c in coins:
    if c > ans:
        break
    ans += c

print(ans)