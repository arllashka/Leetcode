class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        l1 = len(text1)
        l2 = len(text2)
        
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        
        for i in range(l2-1, -1, -1):
            for j in range(l1-1, -1, -1):
                dp[j][i] = dp[j + 1][i + 1] + 1 if text1[j] == text2[i] else max(dp[j + 1][i], dp[j][i + 1])
        return dp[0][0]
        """

        # O(MxN) where M = len(text1) and N = len(text2)
        l1 = len(text1)
        dp = [0]*l1
        for let in text2:
            occur = 0
            for i in range(l1):
                if occur < dp[i]:
                    occur = dp[i]
                elif let == text1[i]:
                    dp[i] = occur + 1
        return max(dp)