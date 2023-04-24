class Solution:
    def numWays(self, n: int, k: int) -> int:
        # O(n)
        # def dp(i):
        #     if i == 1:
        #         return k
        #     if i == 2:
        #         return k*k

        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = (k-1)*(dp(i-1) + dp(i-2))
        #     return memo[i]
            
        # memo = {}
        # return dp(n)

        @lru_cache(None)
        def dp(i):
            if i == 1:
                return k
            if i == 2:
                return k*k

            return (k-1)*(dp(i-1) + dp(i-2))
        
        return dp(n)