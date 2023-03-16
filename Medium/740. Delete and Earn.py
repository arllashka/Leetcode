class Solution:

    # complexity - O(n*logn)
    # n = len(nums)
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = collections.defaultdict(int)
        for num in nums:
            points[num]+=num

        elements = sorted(points.keys())

        twoIndBel = 0
        oneIndBel = points[elements[0]]

        for i in range(1, len(elements)):
            curr = elements[i]

            if curr-1 == elements[i-1]:
                twoIndBel, oneIndBel = oneIndBel, max(twoIndBel + points[curr], oneIndBel)
            else:
                twoIndBel, oneIndBel = oneIndBel, oneIndBel+points[curr]
        
        return oneIndBel