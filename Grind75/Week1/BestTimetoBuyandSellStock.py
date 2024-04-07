# Not Solved) Time Limit Exceeded
class Solution1:
    def maxProfit(prices):
        max_val = 0
        for idx, i in enumerate(prices):
            for j in prices[idx:]:
                if j-i > max_val:
                    max_val=j-i
        return max_val
    
# Solved
class Solution2:
    def maxProfit(prices):
        profit = 0
        buy = prices[0]
        for cur in prices[1:]:
            if buy > cur:
                buy = cur
            profit = max(profit, cur-buy)
        return profit
    

sol = Solution2()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))

"""
Solution1 : Time Limit Exceeded
내 풀이 시간 복잡도 : O(N^2)
문제 Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
=> 10^9이므로 O(N)으로 설계해도 터짐?
=> 1초당 10^8의 연산이 가능한데, LeetCode에는 시간 제한이 안나와있어 애매

Solution2 : Solved
시간 복잡도 : O(N)
사는 가격, 수익 계산은 prices 리스트를 한번 돌 때 같이 계산 가능
"""