class Solution:
    # dp - O(N^2). N - len(prices)
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, isCoolDown, holding):
            if i == len(prices): return 0
            doNothing = dp(i+1, False, holding)
            if isCoolDown: return doNothing
            profit = 0
            
            if holding:
                profit = prices[i] + dp(i+1, True, False)
            else:
                profit = -prices[i] + dp(i+1, False, True)
                
            return max(doNothing, profit)
        
        return dp(0, False, False)