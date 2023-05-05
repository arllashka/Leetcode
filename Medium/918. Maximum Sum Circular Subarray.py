class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax = 0
        curmin = 0
        best = float("-inf")
        worst = float("inf")
        suma = 0
        
        for num in nums:
            curmax = max(curmax+num, num)
            best = max(best, curmax)
            curmin = min(curmin+num, num)
            worst = min(worst, curmin)
            suma+=num
            
            
            
        if suma == worst: 
            return best
        else: 
            return max(best, suma - worst)