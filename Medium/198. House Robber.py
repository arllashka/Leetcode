class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top-Down | Complexity - O(n)
        # memo = {}
        # def dp(n) -> int:
        #     if n == 0: return nums[0]
        #     if n == 1: return max(nums[0], nums[1])
        #     if n not in memo:
        #         memo[n] = max(dp(n-1), dp(n-2)+nums[n])
        #     return memo[n]
        # return dp(len(nums)-1)

        # Bottom-Up | Complexity - O(n)
        leng = len(nums)
        if leng == 1: return nums[0]

        dp = [0] * leng

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, leng):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[leng-1]