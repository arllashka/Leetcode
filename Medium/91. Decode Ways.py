def numDecodings(self, s: str) -> int:
        # O(n), O(n)
        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            if i == len(s)-1:
                return 1

            answer = dp(i + 1)
            if int(s[i : i + 2]) <= 26:
                answer += dp(i + 2)

            return answer
        return dp(0)