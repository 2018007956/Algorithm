n, m = map(int, input().split())
cost = list(int(input()) for _ in range(n))

left, right = min(cost), sum(cost)
while left <= right:
    mid = (left+right)//2 # 인출할 금액
    charge = mid # 현재 가진 돈. 처음 인출.
    cnt = 1 # 인출 횟수
    for c in cost:
        if charge < c: # 가진 돈이 부족하면 돈 인출
            charge = mid
            cnt += 1
        charge -= c # 사용한 만큼 차감

    # m번보다 더 많이 인출하거나 인출한 금액이 하루를 다 살기에 적은 경우 -> 인출 액수 증가 필요
    if cnt > m or mid < max(cost):
        left = mid + 1
    else:
        result = mid
        right = mid - 1

print(result)