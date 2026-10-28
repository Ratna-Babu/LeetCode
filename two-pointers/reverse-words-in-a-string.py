class Solution:
    def reverseWords(self, s: str) -> str:
        right = len(s)-1
        res = []

        while right>=0:
            
            while right >= 0 and s[right] == " ":
                right -= 1
            if right < 0:
                break
            
            left = right
            while right>=0 and s[right]!= " ":
                right -= 1
            
            res.append(s[right+1:left+1])
        
        return " ".join(res)