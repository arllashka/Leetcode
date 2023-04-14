class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @cache
        def dp(i, l, holding):
            if l == 0 or i == len(prices):
                return 0
            
            do_nothing = dp(i+1, l, holding)
            profit = 0
            
            if holding:
                profit = prices[i] + dp(i+1, l-1, 0)
            else:
                profit = -prices[i] + dp(i+1, l, 1)
            
            return max(profit, do_nothing)
        
        return dp(0, k, False)
        # RESOLVE
        # buy = [-inf]*(k+1)
        # sell = [0] *(k+1)
        # for price in prices:
        #     for i in range(1,k+1):
        #         buy[i] = max(buy[i],sell[i-1]-price)
        #         sell[i] = max(sell[i],buy[i]+price)
        # print(buy)
        # print(sell)
        # return sell[-1]