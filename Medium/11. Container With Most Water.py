class Solution:
    def maxArea(self, a: List[int]) -> int:
        # O(n)
        c = 0
        l = 0
        r = len(a)-1     
        while l<r:
            h = min(a[l], a[r])
            c = max(c,h*(r-l))
            # if height[left] <= height[right]:
            #     left += 1
            # else:
            #     right -= 1
            while l < r and h >= a[l]:
                l += 1
            while l < r and h >= a[r]:
                r -= 1  
        return c