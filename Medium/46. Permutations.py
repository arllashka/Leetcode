
class Solution:

    # complexity as same as mathematical permutation formula
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        lis = []
        outp = []

        def dfs(numbers):
            if not numbers:
                outp.append(lis.copy())
            for i in range(len(numbers)):
                n = numbers[i]
                lis.append(n)
                
                del numbers[i]

                dfs(numbers)
                numbers.insert(i, n)
                lis.pop()
        
        dfs(nums)
        return outp