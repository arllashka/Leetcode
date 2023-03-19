
class Solution:
    # Bottom-Up Approach - O(M^2) where M - len(multipliers). 94.56%. Faster because of iterative and skipped half of 2D array
    # left <= i
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        dp = [[0] * (m+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            mult = multipliers[i]
            for left in range(i, -1, -1):
                dp[i][left] = max(nums[left]*mult + dp[i+1][left+1], 
                                  nums[n-1-(i-left)]*mult + dp[i+1][left])
        return dp[0][0]
    
    # Top-Down Approach - O(M^2) where M - len(multipliers). 69.51%
    
    # def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

    #     # Top-Down Approach - O(M^2) where M - len(multipliers)
    #     n = len(nums)
    #     m = len(multipliers)
    #     @lru_cache(2000)
    #     def dp(i, left):
            
    #         if i == m: return 0
            
    #         mul = multipliers[i]
            
    #         right = n - 1 - (i-left)
            
    #         return max(nums[left] * mul + dp(i+1, left+1), nums[right] * mul + dp(i+1, left))
    #     return dp(0, 0)
    
    
