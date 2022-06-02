class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

        for r in range(len(word1)+1):
            dp[0][r] = r
            
        for c in range(len(word2)+1):
            dp[c][0] = c
            
        for x in range(1, len(dp)):
            for y in range(1, len(dp[0])):
                if word1[y-1] == word2[x-1]:
                    dp[x][y] = dp[x-1][y-1]
                    
                else:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1
                    
        return dp[-1][-1]
        
