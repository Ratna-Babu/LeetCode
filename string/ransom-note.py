class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        count = Counter(magazine)

        for ch in ransomNote:
            if ch in magazine:
                if count[ch] == 0:
                    return False
                elif count[ch] > 0:
                    count[ch] -= 1
            else:
                return False
        
        return True
