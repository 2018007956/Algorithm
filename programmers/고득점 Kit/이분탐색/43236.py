# Not Solved
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance
    while left <= right:
        mid = (left+right)//2
        delete = 0 # 제거한 바위 수
        current = 0 # 현재 바위의 위치

        # 제거할 바위 개수 세기
        for rock in rocks:
            dist = rock - current
            # 거리가 커트라인보다 작다면, 바위 제거
            if dist < mid:
                delete += 1
                if delete > n:
                    break
            # 바위를 제거하지 않았다면, current 갱신
            else:
                current = rock

        # 초과 제거한 경우 : 커트라인이 너무 높음
        if delete > n:
            right = mid-1
        # 이하 제거한 경우 : 커트라인이 적절하거나 너무 낮음
        else:
            answer = mid
            left = mid+1
    return answer
'''
input의 최대길이가 지나치게 길고, 특정 값을 찾아야하는 문제라면 이분탐색을 의심해보자

뭘 탐색할 것인가?
이 문제에서는 돌을 n개 제거했을 때의 최소 거리들 중 최대 거리를 구해야 하므로,
최소 거리를 이분 탐색으로 구함
현재 위치와 다음 돌 사이의 거리를 구한 뒤, 이 거리가 mid(=최소 거리)보다 작다면 돌을 제거
    >> 우리는 현재 mid 변수 값을 '문제의 정답'으로 설정한 뒤 풀고 있으므로.

<이분 탐색>
1. 최소 거리(=mid) 설정
2. 그거에 맞게 돌맹이 지워 나감
3. 지워진 돌맹이 개수 확인
4. 문제에서 요구하는 지워야 할 돌맹이 개수랑 똑같은가?
    
ref)
https://oh2279.tistory.com/231
https://jhzlo.tistory.com/76
'''