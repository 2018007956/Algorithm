T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    Floor = N%H 
    Ho = N//H+1
    if N%H == 0:
        Floor = H
        Ho = N//H 
    print(str(Floor)+str(Ho).zfill(2))

'''
N%H==0인 경우를 생각하지 못해서 실패
'''