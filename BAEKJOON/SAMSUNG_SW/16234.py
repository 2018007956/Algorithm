# 풀이 공부 // 다시 풀기
from collections import deque
move = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs():
    pass

N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]

'''
9:45~11:16, 12:30~57 (1h 57m) 
bfs로 모든 인접한 나라 차이 비교
    시작점 인근은 국경선이 안열릴 수도 있음 
    시작점을 하나만 넣지 않고 리스트 돌면서 가능한 값 다 넣는 방식으로 구현

예제 5번 확인
    각 그룹별로 평균 내야함 => How??? 
    풀이 공부 :: queue 왜에 union 리스트 하나 더 사용
    담에 다시 풀어보기
'''