# Not Solved) Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        for idx, i in enumerate(prices):
            for j in prices[idx:]:
                if j-i > max_val:
                    max_val=j-i
        return max_val
"""
첫 번째 시도 : Time Limit Exceeded
내 풀이 시간 복잡도 : O(N^2)
문제 Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
=> 10^9 ?
=> O(N) 으로 설계해야 ?
"""