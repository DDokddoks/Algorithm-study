def solution(food_times, k):
    answer = 0
    i = 0
    time = 0
    finished = set()
    while time < k:
        if food_times[i%len(food_times)] != 0:
            food_times[i%len(food_times)] -= 1
            time += 1
        else:
            finished.add(i%len(food_times))
            if len(finished) == len(food_times):
                return -1
        i += 1
        
    while food_times[i%len(food_times)] == 0:
        i += 1
        
    answer = i%len(food_times) + 1
    return answer