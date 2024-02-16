#23568
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    i, j, k = map(int,str,int,input().split())
    curr_pos = int(input())



'''
1초: 10^8 
n: 10^4이므로 2중 포문 돌려도 시간초과 안남

'''