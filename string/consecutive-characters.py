from collections import Counter
class Solution(object):
    def maxPower(self, s):
        power = 1
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            if count>power:
                power = count
        return power