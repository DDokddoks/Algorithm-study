from collections import deque
def solution(food_times, k):
    answer = 0
    tmp = []
    length = len(food_times)
    for idx, time in enumerate(food_times):
        tmp.append((idx + 1, time))
    dq = deque(tmp)

    sec = 0
    while sec != k + 1:
        num, food = dq[0]
        if answer == -1: break
        answer = num
        if food > 0:
            food -= 1
            dq.popleft()
            dq.append((num, food))
            sec += 1
        else:
            cnt = 0
            while food == 0:
                if cnt == length:
                    answer = -1
                    break
                dq.append(dq.popleft())
                num, food = dq[0]
                answer = num
                cnt += 1
            food -= 1
            dq.popleft()
            dq.append((num, food))
            sec += 1

    if answer == -1:
        return -1
    return answer


print(solution([1], 5))