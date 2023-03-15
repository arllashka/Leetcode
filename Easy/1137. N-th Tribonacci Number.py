class Tribo:
    def __init__(self):
        n = 38
        self.nums = nums = n*[0]
        nums[1]=nums[2]=1
        for i in range(3, n):
            nums[i] = nums[i-1]+nums[i-2]+nums[i-3]

class Solution:
    # complexity - O(1)
    def tribonacci(self, n: int) -> int:
        return Tribo().nums[n]