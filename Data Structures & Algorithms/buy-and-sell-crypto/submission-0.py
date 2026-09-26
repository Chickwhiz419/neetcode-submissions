class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = -1
        max_diff = 0
        for i in range(len(prices)-1,-1,-1):
            curr = prices[i]
            max_diff = max(high - curr,max_diff)
            high = max(curr,high)
        return max_diff


        