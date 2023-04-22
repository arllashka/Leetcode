class Solution:
   # dp solution added
   # @cache
        # def dp(i):
        #     if i<2:
        #         return cost[i]
        #     return cost[i] + min(dp(i-1), dp(i-2))
        # leng=len(cost)-1
        # return min(dp(leng), dp(leng-1))
        
        # O(1) memory
        for i in range (len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])
