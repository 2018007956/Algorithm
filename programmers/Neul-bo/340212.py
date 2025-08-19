def solution(diffs, times, limit):
    answer = 0
    start, end = 1, max(diffs)
    while start <= end:
        level = (start+end)//2
        time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1]

            # if diffs[i] <= level:
            #     time += time_cur
            # else:
            #     time += (diff-level) * (time_cur + time_prev) + time_cur
                
            time += max(0, diff-level) * (time_cur + time_prev) + time_cur

        if time <= limit:
            answer = level
            end = level - 1
        else:
            start = level + 1
            
    return answer