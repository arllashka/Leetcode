class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        best = 0
        
        for price in prices:
            mini = min(price, mini)
            best = max(best, price - mini)
        return best