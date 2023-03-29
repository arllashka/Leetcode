# 221. Maximal Square

class Solution:

    ## Detailed O(mn)
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     rows = len(matrix)
    #     columns = len(matrix[0])

    #     memo = {}

    #     def dp(row, column):

    #         if row >= rows or column >= columns:
    #             return 0
            

    #         if (row, column) not in memo:
    #             down = dp(row+1, column)
    #             right = dp(row, column+1)
    #             diag = dp(row+1, column+1)

    #             memo[(row, column)] = 0

    #             if matrix[row][column] == "1":
    #                 memo[(row, column)] = min(down, right, diag) + 1

    #         return memo[(row, column)]

    #     dp(0,0)

    #     maxi = max(memo.values())

    #     return maxi**2

    ## Classic Top-Down dp => If minimum of 3 adjacent sides is 1, then just added to cell, else add 0. 
    ## Finally get square of maximum value in dp matrix
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rn = len(matrix) # rowNumber
        cn = len(matrix[0]) # columnNumber

        dp = [[0] * (cn+1) for _ in range(rn + 1)]

        for i in range(rn-2, -2, -1):
            for j in range(cn-2, -2, -1):
                if matrix[i+1][j+1] == "1":
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
        
        maxi = max(map(max, dp))

        return maxi**2 