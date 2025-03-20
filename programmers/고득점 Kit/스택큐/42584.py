# 풀이 공부
def solution(prices):
    stack = []
    result = [0] * len(prices)
    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            x = stack.pop()
            result[x] = idx-x
        stack.append(idx)
    
    while stack:
        x = stack.pop()
        result[x] = len(prices)-x-1
        
    return result