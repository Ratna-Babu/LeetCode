class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}

        for ch in s:
            hashmap[ch] = hashmap.get(ch,0) + 1
        
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1

        