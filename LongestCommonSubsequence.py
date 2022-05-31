class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hmap = {}
        def dp(s1, s2, index1, index2):
            if len(s1) == 0 or len(s2) == 0:
                return 0
            
            if (index1, index2) in hmap:
                return hmap[(index1, index2)]
            
            if s1[0] == s2[0]:
                return 1 + dp(s1[1:], s2[1:], index1 + 1, index2 + 1)
            
            else:
                hmap[(index1, index2)] = max(dp(s1, s2[1:], index1, index2 + 1), dp(s1[1:], s2, index1 + 1, index2))
                return hmap[(index1, index2)]
            
        return dp(text1, text2, 0, 0)
