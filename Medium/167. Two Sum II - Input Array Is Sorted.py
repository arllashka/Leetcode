class Solution:
    # Two Pointers - Time Complexity O(n), Space - O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        while left < right:
            su = nums[left] + nums[right]
            if su == target:
                return [left+1, right+1]
            elif su < target:
                left+=1
            elif su > target:
                right-=1