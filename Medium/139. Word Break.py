class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Top-Down Approach O(n⋅k⋅L) where n = s.length, k = wordDict.length, and L is the average length of the words in wordDict

        # @cache
        # def dp(i):
        #     if i < 0: return True
            
        #     for word in wordDict:
                
        #         if ((i >= len(word)-1) and (dp(i-len(word)))):
        #             if s[i-len(word)+1: i+1] in wordDict:
        #                 return True
            
        #     return False
        
        # return dp(len(s) - 1)

        # Bottom-Up Approach O(n⋅k⋅L)
        dp = [False]*len(s)

        for i in range(len(s)):
            for word in wordDict:
                if i>=len(word)-1 and (i == len(word)-1 or dp[i-len(word)]):
                    if s[i-len(word)+1: i+1] == word:
                        dp[i] = True
                        break
        
        return dp[-1]