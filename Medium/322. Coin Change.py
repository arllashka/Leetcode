class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(amountLeft):
            if amountLeft == 0:
                return 0
            
            best = math.inf
            
            for coin in coins:
                if amountLeft >= coin:
                    best = min(best, dp(amountLeft - coin) + 1)
            return best
        
        
        answ = dp(amount)
        
        return answ if answ != math.inf else -1