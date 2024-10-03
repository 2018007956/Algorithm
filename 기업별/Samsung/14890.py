# 
N, L = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

# Row
for road in jido:
    if len(set(road)) == 1:
        cnt += 1
    else:
        pass


# # Column
# for road in zip(*jido):
#     print(road)

'''
4:26~45 (20m) 고민중
    계단 놓는걸 어떻게 구현?
'''