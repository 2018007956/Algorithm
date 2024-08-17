# Solved (20m)
import sys
import bisect
input = sys.stdin.readline

def have(x):
    idx = bisect.bisect_left(cards, x)
    if idx==N or cards[idx]!=x:
        return False
    else:
        return True

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
ques = list(map(int, input().split()))

cards.sort()

for x in ques:
    if have(x):
        print('1', end=' ')
    else:
        print('0', end=' ')

'''
2:56~02 (6m) 10% 런타임에러 (IndexError)
    x가 cards 리스트의 최대 값보다 클 때 bisect.bisect_left(cards, x)로 반환된 idx가 cards 리스트의 유효한 인덱스 범위를 벗어날 수 있음
    cardx[idx]!=x 보다 idx==N 먼저 체크
    
~3:16 (14m) Solved
'''