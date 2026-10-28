class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        s = str(num)
        
        for i in range(len(s)-k+1):
            window = s[i:k+i]
            if int(window)!= 0 and num%int(window)==0:
                res += 1
        return res
