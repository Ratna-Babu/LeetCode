class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        
        for ch in s:
            counter[ch] = counter.get(ch,0) + 1
        
        count = 0
        odd_find = False
        
        for value in counter.values():
            if value%2==0:
                count += value
            else:
                count += value - 1
                odd_find = True
        
        if odd_find:
            count += 1
        
        return count

