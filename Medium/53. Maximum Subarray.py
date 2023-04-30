class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        best = float("-inf")

        for num in nums:
            current = max(num, num+current)
            best = max(current, best)

        return best