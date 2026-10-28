class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            window = s[i:3+i]
            if len(set(window))==3:
                count += 1
        
        return count